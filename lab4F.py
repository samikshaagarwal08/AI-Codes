import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Define the passage
passage = "This is a simple passage with some common stop words."

# Tokenize the passage
words = word_tokenize(passage)

# Get English stop words
stop_words = set(stopwords.words('english'))

# Remove stop words from the passage
filtered_words = [word for word in words if word.lower() not in stop_words]

# Print the filtered words
print("Filtered words:", filtered_words)


# import nltk
# nltk.download('punkt_tab')
