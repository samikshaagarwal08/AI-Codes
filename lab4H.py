import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Define the sentence
sentence = "The cats are running faster than the dogs."

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Create a WordNet Lemmatizer object
lemmatizer = WordNetLemmatizer()

# Define a function to get the part of speech (POS) tag for each word
def get_pos(word):
    # Tagging the word with POS (POS tagging returns tuples like (word, tag))
    pos = nltk.pos_tag([word])[0][1][0].lower()
    if pos in ['a', 'r']:
        return wordnet.ADJ
    elif pos == 'v':
        return wordnet.VERB
    elif pos == 'n':
        return wordnet.NOUN
    else:
        return wordnet.NOUN  # Default to noun if POS tag is unknown

# Lemmatize each word based on its POS tag
lemmatized_words = [lemmatizer.lemmatize(word, get_pos(word)) for word in words]

# Print the original and lemmatized words
print("Original Sentence:", sentence)
print("Lemmatized Words:", lemmatized_words)
