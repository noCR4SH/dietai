import streamlit as st

st.title("Food Advisor")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

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

    response = f"Echo: {prompt}"
    # Display essitant response
    with st.chat_message("assistant"):
        st.markdown(response)
    # add ai response to history
    st.session_state.messages.append({"role": "assistant", "content": response})