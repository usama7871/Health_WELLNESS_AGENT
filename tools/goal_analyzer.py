from guardrails import validate_goal_input
from utils.gemini_api import generate_response
from context import UserSessionContext

def analyze_goal(user_input: str, context: UserSessionContext) -> str:
    prompt = f"""
    You are a health coach analyzing a user's goal: '{user_input}'.
    Extract the quantity, metric, and duration if valid. If unclear, ask for clarification.
    Respond empathetically and conversationally, acknowledging the user's goal.
    """
    gemini_response = generate_response(prompt, context)
    try:
        context.goal = validate_goal_input(user_input)
        response = f"Awesome, {context.name}! You've set a goal to lose {context.goal['quantity']} {context.goal['metric']} in {context.goal['duration']}. {gemini_response}"
        return response
    except ValueError as e:
        return f"Oops, I couldn't quite understand your goal. Could you clarify, e.g., 'I want to lose 5kg in 2 months'? {gemini_response}"