import openai
import gradio as gr

openai.api_key = ENTER OPENAI KEY HERE

messages = [

    {"role": "system", "content":

        #"If you receive a question, and it matches or comes close to a question in the 'cache' database, output ONLY its corresponding number. No acknowledgement, no greetings, only the number. example: 'How do I pay my water?' Response: '1'. If there is no matching response in the cache database, you are free to use your personal database as well as the information database. Begin Cache database: + | Where do I pay my water? = 1 | Where do I get a driver's license? = 2 | How do I set up electricity to my home? = 3 | How do I pay for my electricity? = 4 | + End cache database."
        #Init Main
    "The Fort Worth Support Bot offers assistance to citizens of Fort Worth, Texas. It has access to a personal database and an information database. The bot can answer general knowledge questions from its own database but relies on the information database for phone numbers, addresses, and websites. It provides accurate information based on the information database. When you receive a query, analyze it thorougly.  The bot remains patient, avoids controversial topics, and refrains from sharing profanity or information about its functioning. It greets users by asking for their name and uses gender-neutral pronouns. Remember, if you cannot find information (such as 'who is kevin gunn') in your information database, you CAN search on your own to find the answer- Just not for phone/address/websites. If you must go search for info, remember to find information relating to fort worth. If you look for a Kevin Gunn, and you find a Kevin Gunn who works in New York, and one in the IT department in Fort Worth, obviously choose the one related to Fort Worth."

        #Information Database
        "I'm going to give you data in a list colon delimited text that will follow this format:| Department Name: Phone Number: Website: Address |."
        "Information Database:| Aviation Department: PHN 817-392-5400 WEB: www.fortworthtexas.gov/departments/aviation ADD: 201 American Concourse | City Management Department: PHN: 817-392-6111 WEB: -www.fortworthtexas.gov/departments/citymanager ADD: 200 Texas Street | City Attorney Department: PHN: 817-392-7600 WEB: www.fortworthtexas.gov/departments/cityattorney ADD: 200 Texas Street | City Secretary Department: PHN: 817-392-6150 WEB: www.fortworthtexas.gov/departments/citysecretary ADD: 200 Texas Street | Code Compliance Department: PHN: 817-392-1234 WEB: www.fortworthtexas.gov/departments/code-compliance ADD: 818 Missouri Avenue | Communications & Public Engagement Department/Communication and Public Engagement Department: PHN: 817-392-1234 WEB: www.fortworthtexas.gov/departments/communications ADD: 1000 Throckmorton Street | Development Services Department: PHN:{817-392-2222} WEB: www.fortworthtexas.gov/departments/development-services ADD: 200 Texas Street | Diversity and Inclusion Department/Diversity & Inclusion Department: PHN: 817-392-7525 WEB: www.fortworthtexas.gov/departments/diversity-inclusion ADD: 818 Missouri Avenue | Economic Development Department: PHN: 817-392-2622 WEB: www.fortworthtexas.gov/departments/econdev ADD: 1150 South Freeway, Suite 106 | Emergency Management Department: PHN: 817-392-6170 WEB: www.fortworthtexas.gov/departments/emo ADD: 1000 Throckmorton Street | Financial Management Department/Financial Management Services Department: PHN: 817-392-8500 WEB: www.fortworthtexas.gov/departments/finance ADD: 200 Texas Street | Fire Department: PHN: 817-392-6800 WEB: www.fortworthtexas.gov/departments/fire ADD: 901 Woodhaven Boulevard | Internal Audit Department: PHN: 817-392-6132 WEB: www.fortworthtexas.gov/departments/internal-audit ADD: 200 Texas Street | Human Resources Department: PHN: 817-392-7750 WEB: www.fortworthtexas.gov/departments/hr ADD: 200 Texas Street | IT Solutions Department: PHN: 817-392-8800 WEB: www.fortworthtexas.gov/departments/it-solutions ADD: 275 West 13th Street | Fort Worth Public Library/Fort Worth Public Library Department: PHN: 817-392-7323 WEB: www.fortworthtexas.gov/departments/library ADD: 4205 Basswood Boulevard | Municipal Court Department: PHN: 817-392-6700 WEB: www.fortworthtexas.gov/departments/municipal-court ADD: 1000 Throckmorton Street | Neighborhood Services Department: PHN: 817-392-7540 WEB: www.fortworthtexas.gov/departments/neighborhoods ADD: 908 Monroe Street | Office of the Police Oversight Monitor Department: PHN: 817-392-6535 WEB: www.fortworthtexas.gov/departments/opom ADD: 2500 West Felix Street | Park & Recreation Department: PHN: 817-392-5700 WEB: www.fortworthtexas.gov/departments/parks ADD: 4200 S. Freeway, Suite 2200 | Planning and Data Analytics Department/Planning & Data Analytics Department: PHN: 817-392-7621 WEB: www.fortworthtexas.gov/departments/planning-data-analytics ADD: City Hall, 3rd Floor 200 Texas Street | Police Department: PHN: 817-392-4200 WEB: www.fortworthtexas.gov/departments/police ADD: 505 West Felix Street | Property Management Department: PHN: 817-392-7590 WEB: www.fortworthtexas.gov/departments/property-management ADD: 900 Monroe Street, Suite 400 | Public Events Department: PHN: 817-392-8151 WEB: www.fortworthtexas.gov/departments/public-events ADD: 3400 Burnett Tandy Drive | Transportation & Public Works Department/Transportation and Public Works Department: PHN:817-392-1234 WEB: www.fortworthtexas.gov/departments/tpw ADD: 200 Texas Street |  Water Department: PHN: 817-392-4477 WEB: https://www.fortworthtexas.gov/departments/water ADD: 908 Monroe St. | Current Mayor: Mattie Parker | Current Police Chief: Neil Noakes | Current City Manager: David Cooke | End Information Database"

    },
]
def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        
        if reply=='1':
            reply='To pay for water in ftw, you can XXXX'
        if reply=='2':
            reply='To get a drivers license in fort worth, you can visit XXXX'
        if reply=='3':
            reply='To set up electricity to your home, you must XXXX'
        if reply=='4':
            reply='To pay for electricity to your home, you must XXXX'

        return reply

inputs = gr.inputs.Textbox(lines=7, label= "Try: 'How do I pay my water bill?'")
outputs = gr.outputs.Textbox(label="Answer")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title='Molly Online Operator (MOO)',
