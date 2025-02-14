# AI-Powered Health Assistant

![image](https://github.com/user-attachments/assets/f6fa1ae6-9b05-42b8-92a0-428d8d48b745)

## Overview

The **AI-Powered Health Assistant** is a conversational chatbot designed to provide quick and accessible healthcare advice for general medical queries. It leverages state-of-the-art Natural Language Processing (NLP) technology using the `google/flan-t5-large` model for accurate and real-time responses. The chatbot is built with a user-friendly interface using **Streamlit** and integrates FAQs, memory for conversation history, and dynamic response generation.

> **Disclaimer:** This chatbot provides general healthcare advice and is not a substitute for professional medical consultation. In case of emergencies, consult a licensed medical practitioner immediately.

---

## Features

- **Real-Time Query Responses**: Provides answers to healthcare-related questions, such as symptoms, medications, and appointments.
- **Predefined FAQs**: Quickly responds to common healthcare topics like fever, headaches, and emergencies.
- **Dynamic Text Generation**: Uses the pre-trained `google/flan-t5-large` model for generating responses.
- **Conversation Memory**: Maintains a history of user interactions for a seamless experience.
- **User-Friendly Interface**: Built with Streamlit for easy interaction.
- **Extensible Architecture**: Future enhancements planned for multilingual support, voice interaction, and API integrations.

---

## Demo

Try the chatbot in action! Run it locally by following the setup instructions below.  

![image](https://github.com/user-attachments/assets/ebbec867-5dbf-4fcb-a29e-85a71b10b782)

![image](https://github.com/user-attachments/assets/d57095fd-6a1c-489e-b0ba-53a1156704a1)


---

## Architecture

1. **User Input**: Accepts healthcare-related queries through the Streamlit interface.
2. **FAQ Matching**: Matches predefined FAQs for instant responses.
3. **NLP Model**: Leverages the `google/flan-t5-large` model for generating detailed answers.
4. **Conversation Memory**: Stores user interactions for continuity.
5. **Output**: Displays responses in a clean and intuitive interface.

---

## Requirements

### Hardware
- **Minimum**:
  - CPU: 4 cores
  - RAM: 4 GB (8 GB recommended for smooth processing)
- **Recommended**:
  - GPU: NVIDIA GTX 1650 or higher for faster inference.

### Software
- **Python**: 3.8 or higher
- **Libraries**:
  - `streamlit`
  - `transformers`
  - `torch`

---

## Installation and Setup

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/venkatram-2005/AI-Healthcare-Chatbot.git
   cd AI-Healthcare-Chatbot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate    # On Windows: myenv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

---

## Usage

1. Start the app using the above command.
2. Enter your healthcare query in the input box (e.g., "What are flu symptoms?").
3. View the chatbot's response in real time.
4. Explore the **FAQ Section** in the sidebar for quick answers.
5. Enable the **Conversation History** checkbox to view previous interactions.

---

## Future Work

- **Voice Support**: Integrate speech-to-text and text-to-speech functionality.
- **API Integration**: Add appointment scheduling and medication reminders.
- **Multilingual Support**: Enable users to interact in various languages.
- **Personalized Responses**: Utilize advanced memory mechanisms for tailored advice.

---

## Contributing

Contributions are welcome! If you have ideas to enhance the project, feel free to:
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request.

---

## References

- [Hugging Face Transformers Documentation](https://huggingface.co/docs)
- [Streamlit Documentation](https://docs.streamlit.io)
- [google/flan-t5-large](https://huggingface.co/google/flan-t5-large)
- [PyTorch Documentation](https://pytorch.org/docs)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

This project was completed as part of the **AICTE Internship on AI: Transformative Learning** in collaboration with **TechSaksham** (a joint CSR initiative by Microsoft and SAP). Special thanks to mentors **Jay Rathod** and **Adarsh** for their invaluable guidance and support.
