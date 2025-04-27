import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

responses = {
    "hello": "Hi, how can I assist you today?",
    "how are you": "I'm just a program, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
    "name": "I'm a chatbot created using NLP techniques.",
    "default": "I'm sorry, I didn't understand that."
}

def chatbot(user_input):
    corpus = list(responses.keys())
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus + [user_input.lower()])
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    return responses[corpus[cosine_sim.argmax()]] if cosine_sim.max() > 0.2 else responses["default"]

print("Chatbot: Hello! How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'bye', 'quit']: break
    print(f"Chatbot: {chatbot(user_input)}")
