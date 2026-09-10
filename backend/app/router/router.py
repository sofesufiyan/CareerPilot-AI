def choose_agent(question: str) -> str:
    """
    Classify the student's question and return the chosen agent key.

    Allowed keys:
    - career
    - resume
    - roadmap
    - interview
    - skillgap
    """

    question = question.lower().strip()

    # ==========================================
    # Resume Expert
    # Only for explicit resume analysis requests
    # ==========================================
    resume_phrases = [
        "analyze my resume",
        "analyse my resume",
        "review my resume",
        "review my cv",
        "resume analysis",
        "resume scan",
        "ats score",
        "score my resume",
        "upload resume",
        "upload my resume",
        "review resume",
        "scan my resume",
        "check my resume",
        "evaluate my resume",
    ]

    if any(phrase in question for phrase in resume_phrases):
        print("📄 Selected Agent: Resume Expert")
        return "resume"

    # ==========================================
    # Interview Coach
    # Checked before roadmap because words like
    # "plan" can also appear in interview questions.
    # ==========================================
    interview_keywords = [
        "interview",
        "mock interview",
        "technical interview",
        "hr interview",
        "placement interview",
        "interview questions",
        "prepare for interview",
        "interview preparation",
        "interview prep",
    ]

    if any(keyword in question for keyword in interview_keywords):
        print("🎤 Selected Agent: Interview Coach")
        return "interview"

    # ==========================================
    # Skill Gap Advisor
    # ==========================================
    skill_keywords = [
        "skill gap",
        "missing skills",
        "skill analysis",
        "analyze my skills",
        "analyse my skills",
        "improve my skills",
        "skill assessment",
        "skills i need",
        "skills do i need",
        "skills should i learn",
        "what skills should i learn",
    ]

    if any(keyword in question for keyword in skill_keywords):
        print("📊 Selected Agent: Skill Gap Advisor")
        return "skillgap"

    # ==========================================
    # Learning Planner
    # ==========================================
    roadmap_keywords = [
        "roadmap",
        "learning path",
        "study plan",
        "learning roadmap",
        "career roadmap",
        "learning plan",
        "how to learn",
        "how should i start",
        "what should i learn first",
        "learning schedule",
        "study roadmap",
    ]

    if any(keyword in question for keyword in roadmap_keywords):
        print("🗺️ Selected Agent: Learning Planner")
        return "roadmap"

    # ==========================================
    # Career Mentor (Default)
    # ==========================================
    print("🚀 Selected Agent: Career Mentor")
    return "career"
