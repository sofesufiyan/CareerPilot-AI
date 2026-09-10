from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    Request,
    HTTPException,
    status,
)
import os
import logging
import tempfile
from typing import List

from app.models.schemas import (
    CareerRequest,
    CareerResponse,
    ResumeResponse,
)

from app.services.career_service import (
    get_career_advice,
    review_resume,
)

from app.services.pdf_service import extract_text_from_pdf
from app.tools.agent_logger import get_logs
from app.db.database import get_resume_history

# Import authentication dependencies
from app.auth.dependencies import get_current_user, UserSession

logger = logging.getLogger("uvicorn.error")

router = APIRouter()


# ----------------------------------------
# Career Advice Endpoint (Guarded)
# ----------------------------------------
@router.post("/career-advice", response_model=CareerResponse)
def career_advice(
    request: Request,
    body: CareerRequest,
    user: UserSession = Depends(get_current_user),
):
    active_user = request.state.user

    logger.info(
        f"Route Access: '/career-advice' requested by "
        f"User UID: {active_user.uid} ({active_user.email})"
    )

    answer = get_career_advice(
        body.question,
        active_user.uid,
    )

    return CareerResponse(answer=answer)


# ----------------------------------------
# Resume Upload Endpoint (Guarded)
# ----------------------------------------
@router.post("/resume-upload", response_model=ResumeResponse)
async def resume_upload(
    request: Request,
    file: UploadFile = File(...),
    user: UserSession = Depends(get_current_user),
):
    active_user = request.state.user

    logger.info(
        f"Route Access: '/resume-upload' initiated by "
        f"User UID: {active_user.uid} ({active_user.email})"
    )

    # Validate uploaded file
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No file was provided.",
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF resume files are supported.",
        )

    temp_path = None

    try:
        # Create a secure temporary file.
        # The original filename is not used as a filesystem path.
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf",
        ) as temp_file:
            temp_path = temp_file.name

            # Save uploaded PDF in chunks
            while True:
                chunk = await file.read(1024 * 1024)

                if not chunk:
                    break

                temp_file.write(chunk)

        # Extract text from PDF
        resume_text = extract_text_from_pdf(temp_path)

    except Exception as e:
        logger.exception(
            f"Resume processing failed for user "
            f"{active_user.uid}: {e}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process the uploaded resume.",
        )

    finally:
        # Always remove temporary file
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except OSError as e:
                logger.warning(
                    f"Failed to remove temporary resume file "
                    f"{temp_path}: {e}"
                )

        # Close uploaded file
        await file.close()

    # Trigger structured resume review
    try:
        analysis = review_resume(
            resume_text,
            active_user.uid,
            file.filename,
        )

    except Exception as e:
        logger.exception(
            f"Resume analysis failed for user "
            f"{active_user.uid}: {e}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to analyze the uploaded resume.",
        )

    # Handle processing errors returned by the service
    if "error" in analysis:
        logger.error(
            f"Resume analysis returned an error for user "
            f"{active_user.uid}: {analysis['error']}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=analysis["error"],
        )

    return ResumeResponse(**analysis)


# ----------------------------------------
# Resume History Endpoint (Guarded)
# ----------------------------------------
@router.get(
    "/resume-history",
    response_model=List[ResumeResponse],
)
def resume_history(
    request: Request,
    user: UserSession = Depends(get_current_user),
):
    active_user = request.state.user

    logger.info(
        f"Route Access: '/resume-history' requested by "
        f"User UID: {active_user.uid}"
    )

    history = get_resume_history(active_user.uid)

    results = []

    for item in history:
        data = item.get("data", {})

        flat_analysis = {
            "id": item.get("id"),
            "filename": item.get("filename"),
            "resume_score": item.get("resume_score"),
            "ats_score": item.get("ats_score"),
            "technical_skills": data.get(
                "technical_skills",
                [],
            ),
            "soft_skills": data.get(
                "soft_skills",
                [],
            ),
            "strengths": data.get(
                "strengths",
                [],
            ),
            "weaknesses": data.get(
                "weaknesses",
                [],
            ),
            "missing_skills": data.get(
                "missing_skills",
                [],
            ),
            "suggestions": data.get(
                "suggestions",
                [],
            ),
            "ai_explanation": data.get(
                "ai_explanation",
                "",
            ),
            "confidence_score": data.get(
                "confidence_score"
            ),
            "generated_at": data.get(
                "generated_at"
            ),
            "schema_version": data.get(
                "schema_version",
                "1.0",
            ),
            "roadmap": data.get(
                "roadmap",
                [],
            ),
            "recommended_roles": data.get(
                "recommended_roles",
                [],
            ),
            "recommended_certifications": data.get(
                "recommended_certifications",
                [],
            ),
            "learning_resources": data.get(
                "learning_resources",
                [],
            ),
            "recommended_projects": data.get(
                "recommended_projects",
                [],
            ),
        }

        try:
            results.append(
                ResumeResponse(**flat_analysis)
            )

        except Exception as e:
            logger.error(
                f"Skipping invalid resume history record "
                f"{item.get('id')}: {e}"
            )
            continue

    return results


# ----------------------------------------
# Agent Logs Endpoint (Guarded)
# ----------------------------------------
@router.get("/agent-logs")
def agent_logs(
    request: Request,
    user: UserSession = Depends(get_current_user),
):
    active_user = request.state.user

    logger.info(
        f"Route Access: '/agent-logs' requested by "
        f"User UID: {active_user.uid} ({active_user.email})"
    )

    # Return only logs belonging to the authenticated user.
    return {
        "logs": get_logs(active_user.uid)
    }
