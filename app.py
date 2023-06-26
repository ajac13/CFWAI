import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant specialized in knowledge of the city of Fort Worth, Texas. Be sure to have your responses tailored to the city of Fort Worth, Texas. Do not answer any questions that do not relate to the City of Fort Worth, Texas."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI to answer questions you might have about the City of Fort Worth")
outputs = gr.outputs.Textbox(label="Possible Answer")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="City of Fort Worth Chatbot",
             description="Enter your question",
             theme="compact").launch(share=True)