import os
import google.generativeai as genai
from dotenv import load_dotenv
from context import UserSessionContext

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(prompt: str, context: UserSessionContext) -> str:
    """Generate a conversational response using Gemini API with context."""
    history = "\n".join(
        f"User: {entry['user']}\nAssistant: {entry['agent']}"
        for entry in context.conversation_history[-5:]  # Limit to last 5 interactions
    )
    full_prompt = f"""
    You are a friendly, empathetic Health & Wellness Planner Assistant. Use a conversational tone, acknowledge the user's input, and provide helpful, personalized advice. If appropriate, ask follow-up questions to guide the user. Use the following context and history to tailor your response:

    **User Context**:
    - Name: {context.name}
    - Goal: {context.goal or 'Not set'}
    - Diet Preferences: {context.diet_preferences or 'None'}
    - Injury Notes: {context.injury_notes or 'None'}

    **Conversation History**:
    {history}

    **Current Input**:
    {prompt}

    Respond naturally and helpfully, ensuring the response aligns with the user's health and wellness goals.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(full_prompt)
    return response.text.strip()