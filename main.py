import streamlit as st
from agent import HealthAgent
from context import UserSessionContext
from utils.streaming import stream_response
import sys

def run_cli():
    context = UserSessionContext(name="User", uid=1)
    agent = HealthAgent(context)
    print("Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = agent.run(user_input)
        stream_response(response)

def run_streamlit():
    st.title("Health & Wellness Planner")
    if "context" not in st.session_state:
        st.session_state.context = UserSessionContext(name="User", uid=1)
    if "agent" not in st.session_state:
        st.session_state.agent = HealthAgent(st.session_state.context)
    
    user_input = st.text_input("Enter your message:")
    if user_input:
        response = st.session_state.agent.run(user_input)
        st.write(response)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        run_cli()
    else:
        run_streamlit()