from context import UserSessionContext

def handle_escalation(user_input: str, context: UserSessionContext) -> str:
    context.handoff_logs.append("EscalationAgent")
    return "Connecting you to a human coach..."