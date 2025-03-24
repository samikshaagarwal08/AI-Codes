import re
def chatbot_response(user_input):
    try:
        return str(eval(user_input)) if re.match(r'^[0-9+\-*/().]+$', user_input) else{"hello": "Hi","bye":"Goodbye!","help":"Try '2+2'"}.get(user_input.lower(),"I don't understand")
    
    except:
        return "I can't evaluate that."
    
while(user_input:=input("you: "))!='exit':
    print("bot: ",chatbot_response(user_input))