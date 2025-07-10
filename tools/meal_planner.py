from pydantic import BaseModel
from typing import List
from utils.gemini_api import generate_response
from context import UserSessionContext

class MealPlan(BaseModel):
    days: List[str]

def plan_meal(context: UserSessionContext) -> str:
    prompt = f"""
    Create a 7-day {context.diet_preferences or 'generic'} meal plan tailored to the user's goal: {context.goal or 'general health'}.
    Consider any injury notes: {context.injury_notes or 'none'}.
    Respond conversationally, explaining how the plan supports the user's goals.
    """
    plan_text = generate_response(prompt, context)
    plan = [f"Day {i+1}: {meal}" for i, meal in enumerate(plan_text.split('\n')[:7])]
    context.meal_plan = plan
    return f"Here's your personalized 7-day meal plan, {context.name}! It’s tailored to your {context.diet_preferences or 'general'} preferences and goals:\n{', '.join(plan)}\n{plan_text}"