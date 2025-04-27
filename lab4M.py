import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK datasets
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample sentence
sentence = "NLTK is a leading platform for building Python programs to work with human language data."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Perform POS tagging
pos_tags = nltk.pos_tag(tokens)

# Display the POS tags
print("Sentence:", sentence)
print("POS Tags:", pos_tags)
