# Therapy AI

This is a simple introduction to AI as a Therapist using Gemini API


System Configuration

- pip version - 23.2.1
- python version - 3.9

Project Requirements
- streamlit - to serve the app's presentation layer
- google-generativeai - to integrate the LLM

Installing Dependencies
```commandline
pip install -r requirements.txt --no-cache
```

Running Application

_You need to enter your API key gotten from Google AI Studio in the index file_
```python
genai.configure(api_key=st.secrets.API_KEY)
```

where the API_KEY is being stored in the .streamlit/secrets.toml file like this
```python
API_KEY = '<YOUR_API_KEY>'
```


_Run the application_
```commandline
streamlit run src/index.py
```

Start Chat

_For test purposes, the chat session resets each time you start the server_

The app is being launched in the browser where the user can proceed to chat with the bot

[DEMO](https://therapy-ai-t4cjee9f2hade6a5vflpda.streamlit.app/) | [folorunsodaniel5@gmail.com](mailto:folorunsodaniel5@gmail.com)
