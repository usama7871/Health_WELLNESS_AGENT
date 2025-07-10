from utils.gemini_api import generate_response
from context import UserSessionContext

def recommend_workout(context: UserSessionContext) -> str:
    if not context.goal:
        return "Please set a goal first, like 'I want to lose 5kg in 2 months'."
    prompt = f"""
    Suggest a weekly workout plan for someone with goal: {context.goal}.
    Consider injury notes: {context.injury_notes or 'none'}.
    Respond conversationally, explaining how the plan supports the user's goals.
    """
    plan_text = generate_response(prompt, context)
    plan = {"type": "strength", "days": plan_text.split('\n')[:3]}
    context.workout_plan = plan
    return f"Here's a workout plan tailored for you, {context.name}! It’s designed to help with your goal:\n{plan_text}"