import json
import os
from pydantic import BaseModel
from typing import Optional, List, Dict

class UserSessionContext(BaseModel):
    name: str
    uid: int
    goal: Optional[Dict] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[Dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []
    conversation_history: List[Dict[str, str]] = []

    def save(self, file_path: str = "user_context.json"):
        """Save context to a JSON file."""
        with open(file_path, "w") as f:
            json.dump(self.dict(), f, indent=2)

    @classmethod
    def load(cls, file_path: str = "user_context.json") -> "UserSessionContext":
        """Load context from a JSON file or create a new one if not found."""
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
            return cls(**data)
        except FileNotFoundError:
            return cls(name="User", uid=1)

    def add_conversation(self, user_input: str, agent_response: str):
        """Add a user-agent interaction to conversation history."""
        self.conversation_history.append({"user": user_input, "agent": agent_response})
        self.save()