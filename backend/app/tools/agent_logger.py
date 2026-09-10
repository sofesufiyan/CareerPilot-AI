from typing import Dict, List

# Store logs separately for each authenticated user.
# Example:
# {
#     "firebase_uid_1": ["📥 User Question Received", "🚀 Sending Prompt to Gemini"],
#     "firebase_uid_2": ["📄 Resume Uploaded", "🧠 Resume Agent Started"]
# }
_user_logs: Dict[str, List[str]] = {}


def add(message: str, uid: str) -> None:
    """
    Add a log message for a specific user.
    """
    if not uid:
        return

    if uid not in _user_logs:
        _user_logs[uid] = []

    _user_logs[uid].append(str(message))


def get_logs(uid: str) -> List[str]:
    """
    Return a copy of the logs for a specific user.
    """
    if not uid:
        return []

    return list(_user_logs.get(uid, []))


def clear(uid: str) -> None:
    """
    Clear logs for a specific user.
    """
    if not uid:
        return

    _user_logs.pop(uid, None)
