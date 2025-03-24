# 1. Simple Chatbot using if-else conditions
def simple_chatbot(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm sorry, I don't understand."
            
# Call the simple_chatbot function
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("ChatBot: Goodbye! ")
        break
    print("ChatBot:", simple_chatbot(user_input))