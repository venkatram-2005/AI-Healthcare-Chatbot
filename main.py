import streamlit as st
from transformers import pipeline

# Initialize the healthcare model pipeline
# Using google/flan-t5-large for general healthcare responses
healthcare_pipeline = pipeline(
    "text2text-generation", model="google/flan-t5-large", tokenizer="google/flan-t5-large"
)

# A dictionary to store basic FAQ answers for quick responses
FAQ_RESPONSES = {
    "fever": "Fever can be caused by infections or other medical conditions. Please drink plenty of fluids, rest, and consult a doctor if the fever persists.",
    "headache": "Headaches are common and can result from stress, dehydration, or other causes. Try staying hydrated and resting. Consult a doctor if the headache is severe or persistent.",
    "cough": "Coughing can be caused by colds, allergies, or respiratory issues. Stay hydrated and consult a healthcare provider if it worsens.",
    "emergency": "For any emergencies, immediately contact your local emergency services or visit the nearest hospital.",
}

# Memory for storing previous conversations
conversation_memory = []

# Function to handle healthcare-related queries
def healthcare_chatbot(user_input):
    """
    Main chatbot logic for processing user inputs and generating responses.
    """
    # Check for predefined responses in FAQ
    for keyword, response in FAQ_RESPONSES.items():
        if keyword in user_input.lower():
            return response

    # Predefined responses for specific healthcare-related topics
    if "symptom" in user_input.lower():
        return (
            "I can help you understand common symptoms, but please consult a licensed healthcare professional for accurate advice."
        )
    elif "appointment" in user_input.lower():
        return "Would you like assistance scheduling an appointment with a doctor? Let me know your preferences."
    elif "medication" in user_input.lower():
        return (
            "It's important to take medications as prescribed by your doctor. Let me know if you need information on a specific medicine."
        )

    # Generate dynamic response using the Flan-T5 model for general queries
    return generate_response(user_input)
    

def generate_response(user_input):
    response = healthcare_pipeline(
        user_input, 
        max_length=2000,  # Increase max_length for longer outputs
        num_return_sequences=1, 
        temperature=0.7,  # Slightly lower temperature for better coherence
        top_p=0.9,        # Adjust top_p for diverse responses
        top_k=50,         # Use a reasonable top_k for sampling
        num_beams=5       # Use beam search for longer and coherent outputs
    )
    return response[0]["generated_text"]


# Function to display conversation memory
def display_conversation():
    """
    Displays the entire conversation history for reference.
    """
    st.subheader("Conversation History")
    for entry in conversation_memory:
        st.write(f"**You:** {entry['user']}")
        st.write(f"**Healthcare Assistant:** {entry['bot']}")
        st.write("---")

# Streamlit App - Main function
def main():
    """
    Main function to handle Streamlit UI and interactions.
    """
    st.title("AI Healthcare Assistant Chatbot")
    st.write(
        """
        Welcome! I am an AI-powered healthcare assistant here to provide general advice 
        and answer your healthcare-related questions. For emergencies, please contact 
        a medical professional immediately.
        """
    )

    # Add an FAQ section for quick information
    st.sidebar.header("Quick FAQ")
    st.sidebar.write("Here are some common health topics you can ask about:")
    for keyword in FAQ_RESPONSES.keys():
        st.sidebar.markdown(f"- **{keyword.capitalize()}**")

    # User input for chatbot interaction
    user_input = st.text_input("How can I assist you today?")

    if st.button("Submit"):
        if user_input:
            # Process user input and generate response
            response = healthcare_chatbot(user_input)
            
            # Save conversation to memory
            conversation_memory.append({"user": user_input, "bot": response})

            # Display user input and bot response
            st.write(f"**You:** {user_input}")
            st.write(f"**Healthcare Assistant:** {response}")
        else:
            st.warning("Please enter a query to get a response.")

    # Option to display the conversation history
    if st.checkbox("Show Conversation History"):
        display_conversation()

    # Footer information
    st.write("---")
    st.write("**Disclaimer:** This chatbot provides general healthcare advice and is not a substitute for professional medical consultation.")

if __name__ == "__main__":
    main()
