from utils.gemini_api import generate_response
from context import UserSessionContext

def handle_nutrition_query(user_input: str, context: UserSessionContext) -> str:
    context.handoff_logs.append("NutritionExpertAgent")
    prompt = f"""
    You are a nutrition expert. Provide dietary advice for: '{user_input}'.
    Consider the user's goal: {context.goal or 'none'} and diet preferences: {context.diet_preferences or 'none'}.
    Respond empathetically, offering practical tips and checking if the user has more questions.
    """
    response = generate_response(prompt, context)
    return f"{context.name}, I'm here to help with your dietary needs. {response}"