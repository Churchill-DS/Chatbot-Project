import streamlit as st
import json
import random

# Load the intents data (ensure the path to your intents file is correct)
with open('updated_intents.json', 'r') as f:
    data = json.load(f)


# Function to match user input with patterns and return the correct response
def chatbot_response(user_input_text):
    # Loop through all intents in the data
    for intent in data['intents']:
        # Check if the user input matches any pattern in the current intent
        for pattern in intent['patterns']:
            if user_input_text.lower() == pattern.lower():  # Simple matching (case insensitive)
                bot_response = random.choice(intent['responses'])  # Get a random response for that intent
                return bot_response
    return "Sorry, I didn't understand that."


# Streamlit interface
st.title("Smart Support Chatbot")
st.write("Ask me anything about billing, shipping, or tech support!")

# Display previous conversation
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

# User input
user_input = st.text_input("You: ")

if user_input:
    # Get the chatbot response
    response = chatbot_response(user_input)

    # Add the conversation to the session state
    st.session_state['conversation'].append(f"You: {user_input}")
    st.session_state['conversation'].append(f"Chatbot: {response}")

# Show conversation history
for message in st.session_state['conversation']:
    st.write(message)

# Clear conversation button
if st.button("PRESS ENTER"):
    st.session_state['conversation'] = []