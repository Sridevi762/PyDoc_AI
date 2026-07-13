
import streamlit as st

from database import create_tables
from auth import login_user, register_user

from chat_history import (
    create_chat,
    save_message,
    get_user_chats,
    get_chat_messages,
    delete_chat
)


# -----------------------------
# Create Database
# -----------------------------

create_tables()


# -----------------------------
# Page Config
# -----------------------------


st.set_page_config(
    page_title="PyDoc AI",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)



# -----------------------------
# Session
# -----------------------------

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


if "username" not in st.session_state:

    st.session_state.username = ""


if "user_id" not in st.session_state:

    st.session_state.user_id = None

if "messages" not in st.session_state:

    st.session_state.messages = []


if "current_chat" not in st.session_state:

    st.session_state.current_chat = None


if "selected_question" not in st.session_state:

    st.session_state.selected_question = None


# -----------------------------
# CSS
# -----------------------------

st.markdown("""

<style>

/* Entire browser page background */
html, body, [data-testid="stAppViewContainer"], .stApp {

    background:#EEF5FF;
    min-height:100vh;

}


/* Remove Streamlit top gap and use full page */
.block-container {

    padding-top:0.8rem !important;
    padding-left:0.8rem !important;
    padding-right:1rem !important;
    padding-bottom:0.8rem !important;

    max-width:100% !important;

}


/* Hide Streamlit top header space */
header[data-testid="stHeader"] {

    background:transparent;

}


/* Title */

.login-title{

    text-align:center;
    color:#1565C0;

    font-size:42px;
    font-weight:bold;

    margin-top:20px;
    margin-bottom:5px;

}


/* Subtitle */

.subtitle{

    text-align:center;
    color:#555;

    font-size:18px;
    margin-bottom:30px;

}


/* Sidebar */
section[data-testid="stSidebar"]{

    width:250px !important;
    min-height:100vh;
}

section[data-testid="stSidebar"] > div{

    width:250px !important;
}

/* Remove all extra padding inside sidebar */
section[data-testid="stSidebar"] .block-container{

    padding:0.2rem 0.4rem !important;
}

/* Remove top gap */
section[data-testid="stSidebar"] > div:first-child{

    padding-top:0 !important;
    margin-top:0 !important;
}
            
/* Main content */

.main {

    width:100%;

}

/* Bottom area */
[data-testid="stBottomBlockContainer"]{
    background:#EEF5FF !important;
}

/* Chat input outer container */
div[data-testid="stChatInput"]{
    background:white !important;
    border:1px solid #DADADA !important;
    border-radius:16px !important;
    padding:6px !important;
    box-shadow:none !important;
}

/* All wrappers inside chat input */
div[data-testid="stChatInput"] > div,
div[data-testid="stChatInput"] > div > div{
    background:white !important;
    border:none !important;
}

/* Text area */
div[data-testid="stChatInput"] textarea{
    background:white !important;
    color:black !important;
}

/* Send button */
div[data-testid="stChatInput"] button{
    background:white !important;
    border:none !important;
} 



</style>

""", unsafe_allow_html=True)
# -----------------------------
# Login Page
# -----------------------------

if not st.session_state.logged_in:

    st.markdown(

        "<div class='login-title'>🐍 PyDoc AI</div>",

        unsafe_allow_html=True

    )


    st.markdown(

        "<div class='subtitle'>Python Programming Assistant</div>",

        unsafe_allow_html=True

    )


    login_tab, register_tab = st.tabs(

        [

            "🔑 Login",

            "📝 Register"

        ]

    )


    # -----------------------------
    # Login
    # -----------------------------

    with login_tab:

        username = st.text_input(

            "Username",

            key="login_username"

        )


        password = st.text_input(

            "Password",

            type="password",

            key="login_password"

        )


        if st.button(

            "Login",

            use_container_width=True

        ):

            user_id = login_user(

                username,

                password

            )


            if user_id:

                st.session_state.logged_in = True

                st.session_state.username = username

                st.session_state.user_id = user_id

                st.success("Login Successful!")

                st.rerun()

            else:

                st.error(

                    "Invalid username or password."

                )


    # -----------------------------
    # Register
    # -----------------------------

    with register_tab:

        new_username = st.text_input(

            "Username",

            key="register_username"

        )


        new_password = st.text_input(

            "Password",

            type="password",

            key="register_password"

        )


        if st.button(

            "Register",

            use_container_width=True

        ):

            success = register_user(

                new_username,

                new_password

            )


            if success:

                st.success(

                    "Registration successful! Please login."

                )

            else:

                st.error(

                    "Username already exists."

                )


    st.stop()
from src.chatbot import PyDocAI


# -----------------------------
# Load Chatbot
# -----------------------------

@st.cache_resource
def load_chatbot():

    return PyDocAI()


chatbot = load_chatbot()


# -----------------------------
# Session
# -----------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


if "current_chat" not in st.session_state:

    st.session_state.current_chat = None


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:


    st.markdown("""
        <h2 style="
            color:black;
            margin:0;
            padding:0;
            font-size:28px;
            font-weight:700;
        ">
        🐍 PyDoc AI
        </h2>
        """, unsafe_allow_html=True)

    if st.button(

        "➕ New Chat",

        use_container_width=True

    ):

        st.session_state.messages = []

        st.session_state.current_chat = None

        st.rerun()


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    st.subheader("Recent Chats")


    user_chats = get_user_chats(
        st.session_state.user_id
    )

    if user_chats:

        for chat_id, title in user_chats:

            col1, col2 = st.columns([5, 1])

            with col1:

                if st.button(
                    title,
                    key=f"chat_{chat_id}",
                    use_container_width=True
                ):

                    st.session_state.current_chat = chat_id

                    st.session_state.messages = []

                    messages = get_chat_messages(chat_id)

                    for role, content in messages:

                        st.session_state.messages.append(
                            {
                                "role": role,
                                "content": content
                            }
                        )

                    st.rerun()

            with col2:

                if st.button(
                    "🗑",
                    key=f"delete_{chat_id}"
                ):

                    delete_chat(chat_id)

                    if st.session_state.current_chat == chat_id:

                        st.session_state.current_chat = None
                        st.session_state.messages = []

                    st.rerun()

    else:

        st.caption("No chats yet.")


    st.markdown(
        "<br><br>",
        unsafe_allow_html=True
    )

    if st.session_state.messages:

        txt = ""

        for msg in st.session_state.messages:

            txt += (

                msg["role"].upper()

                + ":\n"

                + msg["content"]

                + "\n\n"

            )


    st.markdown(
        """
        <div style="height:280px;"></div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        f"""
        <div style="
            padding:8px 0;
            font-size:16px;
            font-weight:600;
            color:black;
        ">
            👤 {st.session_state.username}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.user_id = None
        st.session_state.messages = []
        st.session_state.current_chat = None
        st.rerun()
st.title("🐍 PyDoc AI")

st.caption(
        "Python Programming Assistant"
    )
    # -----------------------------
    # Welcome Screen
    # -----------------------------

if len(st.session_state.messages) == 0:

    st.markdown("## 👋 Welcome!")

    st.write(
        """
        I can help you with:

        ✅ Python Basics

        ✅ Functions

        ✅ OOP

        ✅ File Handling

        """
    )

    st.markdown("### 💡 Try asking")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("🐍 What is Python?"):

            st.session_state.selected_question = "What is Python?"

        if st.button("📚 Explain Functions"):

            st.session_state.selected_question = "Explain functions in Python"

        if st.button("🔁 Explain Loops"):

            st.session_state.selected_question = "Explain loops in Python"

    with col2:

        if st.button("🏗️ Explain OOP"):

            st.session_state.selected_question = "Explain Object Oriented Programming"

        if st.button("📂 File Handling"):

            st.session_state.selected_question = "Explain file handling in Python"

        if st.button("⚠️ Exception Handling"):

            st.session_state.selected_question = "Explain exception handling in Python"

    # -----------------------------
# Display Previous Messages
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])
# -----------------------------
# Chat Input
# -----------------------------

question = st.chat_input(
    "Ask a Python question..."
)
if st.session_state.selected_question:

    question = st.session_state.selected_question

    st.session_state.selected_question = None

# -----------------------------
# Ask Chatbot
# -----------------------------

if question:

    # Create a new chat if needed
    if st.session_state.current_chat is None:

        st.session_state.current_chat = create_chat(

            st.session_state.user_id,

            question[:40]

        )


    # -----------------------------
    # User Message
    # -----------------------------

    with st.chat_message("user"):

        st.write(question)


    st.session_state.messages.append(

        {
            "role": "user",
            "content": question
        }

    )


    # Save user message
    save_message(

        st.session_state.current_chat,

        "user",

        question

    )


    # -----------------------------
    # Assistant
    # -----------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = chatbot.ask(question)

        st.write(answer)


    st.session_state.messages.append(

        {
            "role": "assistant",
            "content": answer
        }

    )


    # Save assistant reply
    save_message(

        st.session_state.current_chat,

        "assistant",

        answer

    )
