import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant specialized in knowledge of the city of Fort Worth, Texas. Be sure to have your responses tailored to the city of Fort Worth, Texas. Do not answer any questions that do not relate to the City of Fort Worth, Texas. If any irrelevant question is asked, such as 'what is water', attempt to relate them to the city's infrastructure and if impossible then say 'I am sorry, I do not understand.' For example, the correct response to 'what is water' is 'water is a department of the city of fort worth'. Do not preface this type of response with 'in the context of fort worth...', rather say 'in fort worth,'"},
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

inputs = gr.inputs.Textbox(lines=7, label= "Try: 'How do I pay my water bill?'")
outputs = gr.outputs.Textbox(label="Answer")

gr.Interface( fn=chatbot, inputs=inputs, outputs=outputs, title="City of Fort Worth Community Support",
             description="Ask any questions you might have about the City of Fort Worth",
             theme="Glass").launch(share=True)
