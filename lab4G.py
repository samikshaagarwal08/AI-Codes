import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')

# Define the sentence
sentence = "Running runners run very fast."

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Create a Porter Stemmer object
stemmer = PorterStemmer()

# Apply stemming to each word
stemmed_words = [stemmer.stem(word) for word in words]

# Print the original and stemmed words
print("Original Sentence:", sentence)
print("Stemmed Words:", stemmed_words)
