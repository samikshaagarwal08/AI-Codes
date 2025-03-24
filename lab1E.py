import requests 
import json

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/blenderbot-400M-distill"
HEADERS = {
        "Authorization": "Bearer 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", 
        "Content-Type": "application/json"
}

def chat_with_huggingface(prompt):
    payload = json.dumps({"inputs": prompt})
    
    try:
        response = requests.post(API_URL, headers=HEADERS, data=payload)
        response.raise_for_status()  # Raise an error for HTTP issues (4xx, 5xx)
        data = response.json()

        # Check if response contains generated text
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        else:
            return "Error: Unexpected response format from Hugging Face API."

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def main():
    print("Chatbot (Hugging Face) is ready! Type 'exit' to stop.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = chat_with_huggingface(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
