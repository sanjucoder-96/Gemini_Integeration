import google.generativeai as genai
import os
import json
import process

my_api_key = os.getenv("GEMINI_API_KEY")


def gemini_ai(command):
    filename = "rules.json"
    

    with open(filename, 'r') as file:
            r = json.load(file)

    genai.configure(api_key=my_api_key)

    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    prompt=f"""  You are an advanced AI assistant that can either answer questions directly or provide certain fixed commands which are in a rulebook.
        here is the list of rules according to which you need to answer . it is in JSON format:{r}
        You need to follow the below instructions strictly
        Firstly identify the command from the list which closely matches the user's request.
        check the action field of that command. if the action  command is self. Respond with a JSON style text in the format :{{"code":"general","answer":" write the answer here...."}} 
         otherwise respond with a JSON style text object which contains the code followed by the parameters if any exist like in this format {{"code":"navigate","parameters":{{"foldername":"downloads"}}}}.
         you should not add any text apart from what i mentioned above. your response should be a valid JSON text like object
             
        User Request: "{command}"""
    response = model.generate_content(prompt)
      
    return process.process_command(response.text)
