import streamlit as st
import random
from ai_client import get_ai_response
from logger import log_interaction
from profile_data import profile_info
from errors import AIClientError

# ---------------------------
# 1️⃣ Page setup
# ---------------------------
st.set_page_config(page_title="Tendo's AI Helper 2026", page_icon="🤖", layout="wide")

# ---------------------------
# 2️⃣ Sidebar branding (ADD THIS HERE)
# ---------------------------
# Sidebar minimal branding
st.sidebar.image("assets/profile.png", width=150)
st.sidebar.title("Tendo's AI Helper 2026")
st.sidebar.write("Agentic AI Engineer & Systems Administrator")
st.sidebar.subheader("Connect with Tendo 💬")

# Social buttons
if st.sidebar.button("LinkedIn"):
    js = "window.open('https://www.linkedin.com/in/tendo-taliq-5a66b02bb/')"  # opens link
    st.components.v1.html(f"<script>{js}</script>")

if st.sidebar.button("X / Twitter"):
    js = "window.open('https://x.com/TendoTaliq')"
    st.components.v1.html(f"<script>{js}</script>")


# ---------------------------
# 3️⃣ Session state and greetings
# ---------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if not st.session_state.history:
    greeting = random.choice(profile_info['greetings'])
    st.write(greeting)

# ---------------------------
# 4️⃣ Chat input
# ---------------------------
user_input = st.text_input("Ask your question:")

if st.button("Ask Tendo"):
    if not user_input.strip():
        st.warning("Please type a question!")
    else:
        try:
            answer = get_ai_response(user_input)
            st.success(answer)
            log_interaction(user_input, answer)
            
            # Reset chat for new session
            st.session_state.history = []
        except AIClientError as e:
            st.error(f"Error: {str(e)}")


# ---------------------------
# 5️⃣ Conversation history
# ---------------------------
if st.session_state.history:
    st.markdown("---")
    st.subheader("Conversation History")
    for item in st.session_state.history:
        st.markdown(f"**Q:** {item['Q']}")
        st.markdown(f"**A:** {item['A']}")
        st.markdown("---")
