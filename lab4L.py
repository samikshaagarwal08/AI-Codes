import nltk
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize

# Download necessary NLTK datasets
nltk.download('stopwords')
nltk.download('punkt')

# Sample dataset (SMS Spam Collection)
data = [
    ("Free entry in 2 a wkly comp to win FA Cup final tkts", "spam"),
    ("Nah I don't think he goes to usf, he lives around here though", "ham"),
    ("FreeMsg: Hey there! We tried to contact you. Reply for free", "spam"),
    ("I'm gonna be home soon and i don't want to talk to you", "ham"),
    ("WINNER!! You have won a $1000 Walmart gift card. Click to claim", "spam"),
    ("I have a meeting tomorrow, let's reschedule", "ham")
]

# Preprocess text: tokenizing and removing stopwords
def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text.lower())
    return {word: True for word in tokens if word.isalpha() and word not in stop_words}

# Create feature sets
train_set = [(preprocess_text(text), label) for (text, label) in data[:4]]
test_set = [(preprocess_text(text), label) for (text, label) in data[4:]]

# Train Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Test the classifier
accuracy = nltk.classify.accuracy(classifier, test_set)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Function to classify new message
def classify_message(message):
    features = preprocess_text(message)
    return classifier.classify(features)

# Test with new input
test_message = "Congratulations, you've won a prize! Call now to claim."
print(f"Message: {test_message}")
print(f"Classified as: {classify_message(test_message)}")
