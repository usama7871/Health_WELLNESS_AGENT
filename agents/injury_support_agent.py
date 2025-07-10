from utils.gemini_api import generate_response
from context import UserSessionContext

def handle_injury_support(user_input: str, context: UserSessionContext) -> str:
    context.handoff_logs.append("InjurySupportAgent")
    context.injury_notes = user_input
    prompt = f"""
    You are an injury support specialist. Suggest safe exercises for someone with: '{user_input}'.
    Consider their goal: {context.goal or 'none'}.
    Respond conversationally, offering safe options and checking if the user needs more guidance.
    """
    response = generate_response(prompt, context)
    return f"Sorry to hear about your injury, {context.name}. {response}"