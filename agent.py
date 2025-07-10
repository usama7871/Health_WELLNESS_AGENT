from tools.goal_analyzer import analyze_goal
from tools.meal_planner import plan_meal
from tools.workout_recommender import recommend_workout
from tools.scheduler import schedule_checkin
from tools.tracker import track_progress
from agents.escalation_agent import handle_escalation
from agents.nutrition_expert_agent import handle_nutrition_query
from agents.injury_support_agent import handle_injury_support
from utils.gemini_api import generate_response
from context import UserSessionContext

class HealthAgent:
    def __init__(self, context: UserSessionContext):
        self.context = context
        self.tools = {
            "goal": analyze_goal,
            "meal": plan_meal,
            "workout": recommend_workout,
            "schedule": schedule_checkin,
            "progress": track_progress
        }
        self.agents = {
            "escalation": handle_escalation,
            "nutrition": handle_nutrition_query,
            "injury": handle_injury_support
        }
        self.state = "initial"  # States: initial, goal_set, planning, tracking

    def _update_state(self, user_input: str):
        """Update agent state based on user input and context."""
        user_input = user_input.lower()
        if "lose" in user_input or "gain" in user_input:
            self.state = "goal_set"
        elif "diet" in user_input or "vegetarian" in user_input or "meal" in user_input:
            self.state = "planning"
        elif "workout" in user_input:
            self.state = "planning"
        elif "progress" in user_input:
            self.state = "tracking"
        elif "schedule" in user_input:
            self.state = "planning"
        elif "diabetes" in user_input or "allergy" in user_input or "pain" in user_input or "injury" in user_input:
            self.state = "specialized"
        elif "human" in user_input or "trainer" in user_input:
            self.state = "escalation"

    def _generate_follow_up(self) -> str:
        """Generate follow-up questions based on state."""
        if self.state == "initial":
            return "What health goal would you like to set today? For example, 'I want to lose 5kg in 2 months'."
        elif self.state == "goal_set":
            return "Great! Would you like a meal plan, workout plan, or to schedule a check-in?"
        elif self.state == "planning":
            return "Anything else I can help with? Maybe track progress or address specific needs like injuries?"
        elif self.state == "tracking":
            return "Thanks for updating your progress! Want to see a meal or workout plan next?"
        elif self.state == "specialized":
            return "Do you have any other specific needs or would you like to continue with a plan?"
        return ""

    def run(self, user_input: str) -> str:
        """Orchestrate the agent workflow with state management and follow-up prompts."""
        self._update_state(user_input)
        user_input_lower = user_input.lower()

        # Handle specialized agent handoffs
        if "diabetes" in user_input_lower or "allergy" in user_input_lower:
            response = self.agents["nutrition"](user_input, self.context)
        elif "pain" in user_input_lower or "injury" in user_input_lower:
            response = self.agents["injury"](user_input, self.context)
        elif "human" in user_input_lower or "trainer" in user_input_lower:
            response = self.agents["escalation"](user_input, self.context)
        # Handle tool calls
        elif "lose" in user_input_lower or "gain" in user_input_lower:
            response = self.tools["goal"](user_input, self.context)
        elif "vegetarian" in user_input_lower or "diet" in user_input_lower or "meal" in user_input_lower:
            self.context.diet_preferences = "vegetarian" if "vegetarian" in user_input_lower else "generic"
            response = self.tools["meal"](self.context)
        elif "workout" in user_input_lower:
            response = self.tools["workout"](self.context)
        elif "progress" in user_input_lower:
            response = self.tools["progress"](user_input, self.context)
        elif "schedule" in user_input_lower:
            response = self.tools["schedule"](self.context)
        else:
            # Fallback to Gemini for general queries
            response = generate_response(user_input, self.context)

        # Append follow-up question
        follow_up = self._generate_follow_up()
        if follow_up:
            response += f"\n{follow_up}"

        # Save conversation to history
        self.context.add_conversation(user_input, response)
        return response