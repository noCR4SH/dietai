import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from ai import chat

if "messages" not in st.session_state:
    st.session_state.messages = []

col1, col2 = st.columns([2, 1])

with col1:
    st.title("Food Advisor")

with col2:
    with stylable_container(
        key="clear_chat_button",
        css_styles="""
        button {
            float: right;
        }
        """
        ):
        if st.button("🔄", type="primary"):
            st.session_state.messages = []


# Initialize chat history in session state

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
# prompt = st.chat_input("What's up?")
# if prompt:
# rest of the code

if prompt := st.chat_input("What's up?"):
    # Display user message in chat container
    st.chat_message("user").markdown(prompt)
    # Add user mesage to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate AI response
    response = chat.generate_response(prompt, st.session_state.messages)

    # Display essitant response
    with st.chat_message("assistant"):
        st.markdown(response)
    # add ai response to history
    st.session_state.messages.append({"role": "assistant", "content": response})