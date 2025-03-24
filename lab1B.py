import random 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

training_data={"greeting":["Hello","Hi"],
                "bye": ["Bye", "See You"]}
responses={"greeting":["Hello!"],
                "bye": ["GoodBye!"]}

vectorizer=CountVectorizer()
X_train = sum(training_data.values(),[])
y_train = sum([[tag]*len(phrases) for tag,phrases in training_data.items()],[])
model = MultinomialNB().fit(vectorizer.fit_transform(X_train), y_train)

def chatbot_response(user_input):
    return random.choice(responses.get(model.predict(vectorizer.transform([user_input]))[0]))

while(user_input:= input("you: "))!='exit':
    print("Bot: ", chatbot_response(user_input))