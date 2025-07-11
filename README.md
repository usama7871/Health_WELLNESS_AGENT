
# Health & Wellness Planner Agent

## Project Overview
The Health & Wellness Planner Agent is a conversational AI application designed to assist users in setting and achieving health and fitness goals. Built with Python 3.12.10 and powered by the Gemini API, it simulates the functionality of the OpenAI Agents SDK (without requiring a paid OpenAI API key). The agent supports multi-turn conversations, persistent memory, and context-aware responses, making it a professional health and wellness assistant. Key features include:

- **Goal Setting**: Parse and validate user goals (e.g., "Lose 5kg in 2 months").
- **Personalized Plans**: Generate 7-day meal plans and workout recommendations based on user preferences and goals.
- **Progress Tracking**: Log user progress and schedule check-ins.
- **Specialized Handoffs**: Delegate complex queries to Nutrition Expert or Injury Support agents.
- **Persistent Memory**: Save conversation history and user context to `user_context.json`.
- **Conversational Interface**: Empathetic, natural responses with follow-up questions.
- **Dual Interface**: Run via command-line interface (CLI) or Streamlit web interface.

The project uses UV for fast package management, Pydantic for input/output guardrails, and a modular structure for extensibility. It’s optimized for Windows and tested on Windows 10 (Version 10.0.19045.5965).

## Project Structure
```
D:\ASSIGNMENT_GIAIC\01\health_wellness_agent\
├── main.py                  # Entry point for CLI and Streamlit
├── agent.py                 # Main HealthAgent for orchestration
├── context.py               # Persistent UserSessionContext with memory
├── guardrails.py            # Input/output validation
├── tools\                   # Tool implementations
│   ├── goal_analyzer.py
│   ├── meal_planner.py
│   ├── workout_recommender.py
│   ├── scheduler.py
│   ├── tracker.py
├── agents\                  # Specialized agent implementations
│   ├── escalation_agent.py
│   ├── nutrition_expert_agent.py
│   ├── injury_support_agent.py
├── utils\                   # Utility functions
│   ├── gemini_api.py        # Gemini API integration
│   ├── streaming.py         # Real-time response streaming
├── .env                     # Gemini API key storage
├── .python-version          # UV Python version pin
├── pyproject.toml           # Dependency and build configuration
├── README.md                # This file
├── user_context.json        # Persistent user context (generated)
```

## Prerequisites
- **Windows 10 or later**: Tested on Windows 10 (Version 10.0.19045.5965).
- **UV**: Python package manager for fast dependency management.
- **Python 3.12.10**: Specified for compatibility with dependencies.
- **Gemini API Key**: Free key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Setup Instructions (Windows)
Follow these steps to set up the project on Windows:

1. **Install UV**:
   Open Command Prompt and run:
   ```
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   If `curl` fails, download the UV installer from [astral.sh](https://astral.sh/uv/install) and run it manually.

2. **Navigate to Project Directory**:
   ```
   cd D:\ASSIGNMENT_GIAIC\01\health_wellness_agent
   ```

3. **Pin Python 3.12.10**:
   Ensure UV uses Python 3.12.10:
   ```
   uv python pin 3.12.10
   ```
   If Python 3.12.10 is not installed, UV will download it automatically.

4. **Create Virtual Environment**:
   ```
   uv venv --python 3.12.10
   .\.venv\Scripts\activate
   ```

5. **Install Dependencies**:
   The `pyproject.toml` specifies all dependencies. Sync them with:
   ```
   uv sync
   ```
   Contents of `pyproject.toml`:
   ```
   [project]
   name = "health-wellness-agent"
   version = "0.1.0"
   description = "A conversational AI-powered Health & Wellness Planner using Gemini API"
   readme = "README.md"
   requires-python = ">=3.12,<3.13"
   dependencies = [
       "google-generativeai==0.8.3",
       "pydantic==2.9.2",
       "streamlit==1.39.0",
       "python-dotenv==1.0.1",
   ]

   [build-system]
   requires = ["hatchling"]
   build-backend = "hatchling.build"

   [tool.hatch.build.targets.wheel]
   packages = ["."]
   ```

6. **Set Gemini API Key**:
   Create a `.env` file in `D:\ASSIGNMENT_GIAIC\01\health_wellness_agent`:
   ```
   GEMINI_API_KEY=your-api-key-here
   ```
   Replace `your-api-key-here` with a key from [Google AI Studio](https://aistudio.google.com/app/apikey).

7. **Suppress Hardlink Warning**:
   To avoid UV’s “Failed to hardlink files” warning:
   ```
   set UV_LINK_MODE=copy
   ```

## Running the Application
The project supports two interfaces: CLI and Streamlit.

### CLI Mode
1. Activate the virtual environment:
   ```
   cd D:\ASSIGNMENT_GIAIC\01\health_wellness_agent
   .\.venv\Scripts\activate
   ```

2. Run the CLI:
   ```
   uv run python main.py --cli
   ```

3. Interact with the agent by typing commands:
   - "I want to lose 5kg in 2 months" → Sets a goal and saves to `user_context.json`.
      - Example response: "Awesome, User! You've set a goal to lose 5.0 kg in 2 months. Great! Would you like a meal plan, workout plan, or to schedule a check-in?"
   - "I’m vegetarian" → Generates a personalized meal plan.
   - "I have knee pain" → Triggers Injury Support Agent with safe exercise suggestions.
   - "I’m diabetic" → Triggers Nutrition Expert Agent with dietary advice.
   - "Talk to a trainer" → Triggers Escalation Agent.
   - Type `exit` to quit.

   Responses are streamed in real-time, and conversation history is saved to `user_context.json`.

### Streamlit Mode
1. Activate the virtual environment (if not already active):
   ```
   cd D:\ASSIGNMENT_GIAIC\01\health_wellness_agent
   .\.venv\Scripts\activate
   ```

2. Run the Streamlit app:
   ```
   uv run streamlit run main.py
   ```

3. Open the provided URL (e.g., `http://localhost:8501`) in a web browser.
4. Enter commands in the text input field (same as CLI examples above). Responses are displayed conversationally with follow-up questions.

## Features
- **Persistent Memory**: User context and conversation history are saved to `user_context.json`, loaded on startup for seamless session continuity.
- **Natural Interaction**: Empathetic, personalized responses using the user’s name and context-aware follow-up questions (e.g., “Would you like a meal plan next?”).
- **Sophisticated Orchestration**: A state machine (`initial`, `goal_set`, `planning`, `tracking`, `specialized`, `escalation`) ensures intelligent task prioritization and handoffs to specialized agents.
- **Guardrails**: Pydantic models validate inputs (e.g., goal format) and outputs (e.g., meal plans).
- **Gemini API**: Powers natural language understanding and response generation, simulating OpenAI Agents SDK functionality without a paid OpenAI API key.

## Example Usage
```
CLI:
You: I want to lose 5kg in 2 months
Agent: Awesome, User! You've set a goal to lose 5.0 kg in 2 months. This plan looks achievable! Great! Would you like a meal plan, workout plan, or to schedule a check-in?

You: I’m vegetarian
Agent: Here's your personalized 7-day meal plan, User! It’s tailored to your vegetarian preferences and goals: Day 1: Lentil Soup, Day 2: Veggie Stir-Fry, ... Anything else I can help with? Maybe track progress or address specific needs like injuries?

Streamlit:
[Enter in browser]: I have knee pain
[Response]: Sorry to hear about your injury, User. For knee pain, try low-impact exercises like swimming or stationary cycling. Do you have any other specific needs or would you like to continue with a plan?
```

## Troubleshooting
- **Gemini API Errors**: Verify the `GEMINI_API_KEY` in `.env`. Regenerate the key from [Google AI Studio](https://aistudio.google.com/app/apikey) if you get a `403` error.
- **Import Errors**: Ensure all files (`main.py`, `agent.py`, etc.) are in the correct directories and match the provided code.
- **Streamlit Issues**: Confirm `streamlit==1.39.0` is installed (`uv pip list`). If the app doesn’t load, try `uv run streamlit run main.py --server.port 8502`.
- **UV Errors**: If `uv sync` fails, recreate the environment:
  ```
  rmdir /s /q .venv
  uv venv --python 3.12.10
  uv sync
  ```
- **Python Version**: Verify Python 3.12.10 is used (`uv python list`). If issues persist, reinstall with `uv python install 3.12.10`.

## Notes
- **OpenAI Agents SDK**: The project simulates the SDK’s functionality (tool calls, handoffs, state management) using the `HealthAgent` class, as no paid OpenAI API key is available. If you have access to a specific SDK version or free tier, provide details for integration.
- **Date**: Tested as of July 11, 2025, 09:37 AM PKT.
