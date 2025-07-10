from context import UserSessionContext
def track_progress(user_input: str, context: UserSessionContext) -> str:
    log = {"date": "today", "note": user_input}
    context.progress_logs.append(log)
    return f"Progress logged: {user_input}"