from pydantic import BaseModel, ValidationError

class GoalInput(BaseModel):
    quantity: float
    metric: str
    duration: str

def validate_goal_input(user_input: str) -> dict:
    try:
        parts = user_input.split()
        quantity = float(parts[2])  # e.g., "5" in "lose 5kg"
        metric = parts[3]           # e.g., "kg"
        duration = " ".join(parts[5:])  # e.g., "2 months"
        goal = GoalInput(quantity=quantity, metric=metric, duration=duration)
        return goal.dict()
    except (IndexError, ValueError, ValidationError):
        raise ValueError("Invalid goal. Try: 'I want to lose 5kg in 2 months'.")