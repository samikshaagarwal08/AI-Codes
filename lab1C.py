# 3. Chatbot with predefined knowledge base
import random 

knowledge_base = {
    "hello":"Hi there! How can I help you?",
    "name": "I am a Chatbot created to assist you.",
    "help": "Sure! What do you need help with?",
    "bye": "Goodbye!Have a great day!"
}

def chatbot_response(user_input):
    return knowledge_base.get(user_input.lower(),"I am not sure how to respond to that.")

while(user_input:=input("you: "))!='exit':
    print("Bot: ", chatbot_response(user_input))