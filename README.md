# Health & Wellness Planner Agent
A conversational AI using Gemini API and UV Python for health goal planning.

## Setup
1. Install UV: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Create project: `uv init`, `uv python install 3.12`, `uv venv`, `source .venv/bin/activate`
3. Install dependencies: `uv pip install -r requirements.txt`
4. Set Gemini API key in `.env`: `GEMINI_API_KEY=your-api-key`
5. Run CLI: `uv run python main.py --cli`
6. Run Streamlit: `uv run streamlit run main.py`

## Usage
- Set a goal: "I want to lose 5kg in 2 months"
- Request a plan: "I’m vegetarian" or "Give me a workout"
- Track progress: "Progress: Ran 5km today"