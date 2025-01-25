import streamlit as st
import google.generativeai as genai

st.title("Therapy Bot")
st.subheader("Your Mental Health Assistant")

genai.configure(api_key=st.secrets.API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-8b",
                              system_instruction=[
                                  "You are a therapist but the user does not need to know that, but be friendly, "
                                  "people need good vibes",
                                  "Your responses should not be more than 4 lines at a go",
                                  "If you notice something that requires human intervention, provide helplines to "
                                  "reach out to",
                                  "Adhere to HIPAA Policies",
                                  "If there first aid exercises to carry out in the case of emergencies please "
                                  "provide suggestions"
                              ])
chat = model.start_chat()


def send_message(message=""):
    response = chat.send_message(content=message)
    result = response.text
    return result


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Type a message"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = send_message(message=prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
