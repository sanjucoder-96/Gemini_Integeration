import json
from functions import function,none
import pyttsx3
from main import speak
from functions import none

def process_command(response):
    output=response.strip()
    output=output.replace("```json","").replace("```","").strip()


    res_dict=json.loads(output);
    keys_list=res_dict.keys();

    if("answer" in keys_list):
        speak(res_dict["answer"])
        return
    command_code=res_dict["code"]
    params=res_dict.get("parameters",{})
    task=function.get(command_code,none)

    if(params!={}):
        return (task(**params))
    else:
      return task()



    
    
      