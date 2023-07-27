# City of Fort Worth Community Support Chatbot
By: Allen Jacob, John Allister, Ian Utz, Yousif Krblaae, Gabriela Cazares for IT Solitions, City of Fort Worth

This is a Python script that implements a chatbot using the GPT-3.5-turbo language model from OpenAI. The chatbot serves as a community support assistant for the City of Fort Worth, Texas, providing information and answering questions related to various city departments and services. 

## Prerequisites

Before running the code, make sure you have the following installed:

- Python 3.x
- [OpenAI Python API](https://pypi.org/project/openai/)
- [Gradio](https://www.gradio.app/)
- [OpenAI Accoutn with Credits](https://openai.com/pricing)

## Getting Started

1. Install the required libraries by running:
   ```
   pip install openai gradio
   ```

2. Set up the OpenAI API key:
   Replace the placeholder in app.py line 4 `ENTER OPENAI KEY HERE in the code with your actual OpenAI API key.

3. Launch the chatbot:
   Execute the Python script to start the Gradio interface for the City of Fort Worth Community Support chatbot. The chatbot will be accessible through a local web interface.

## How to Use

1. Open the Terminal and run the below command. Simply enter python, add a space, paste the path (right-click to quickly paste), and hit Enter.
```
python "C:\Users\mearj\Desktop\app.py"
```
2. You may get a few warnings, but ignore them. At the bottom, you will get a local and public URL. Now, copy the local URL and paste it into the web browser.

3. Enter your questions or queries in the input text box.

4. Click on the "Submit" button or press Enter to submit your question.

5. The chatbot will respond with relevant information and answers related to the City of Fort Worth.

## Security Rules

- The chatbot follows specific security rules to protect sensitive information. This is just test code for proof of concept. Anything from here must not be sent to the public. 

## Note

- The chatbot interface has been themed using the "dracula_revamped" theme for a visually appealing experience. This can be altered using gradio.

## Example

Try asking the chatbot: "How do I pay my water bill?"

## Disclaimer

This chatbot is designed to provide general assistance and information related to the City of Fort Worth. While it follows strict security rules to protect sensitive data, it may not cover all possible scenarios. For any critical or official inquiries, please contact the City of Fort Worth directly through official channels.

## Credits

- This code utilizes the GPT-3.5-turbo model from OpenAI for natural language processing and conversation generation.
- The web interface is built using Gradio, an interactive interface creator for machine learning models.
- [Beebom.com](https://beebom.com/how-build-own-ai-chatbot-with-chatgpt-api/)

**Note:** The code provided here assumes that you have the necessary permissions and access rights to use the OpenAI API and the data from the City of Fort Worth. Make sure to comply with any legal and ethical considerations before deploying the chatbot in any production environment.
