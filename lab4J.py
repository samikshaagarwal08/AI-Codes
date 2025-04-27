import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Define the text to summarize
text = """
Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans using natural language. The ultimate goal of NLP is to enable machines to understand, interpret, and generate human language in a way that is valuable. NLP involves several challenges including language modeling, machine translation, sentiment analysis, and text summarization.
Text summarization is one of the important tasks in NLP. It refers to the process of condensing a large piece of text into a shorter summary, preserving the most critical information. Summarization can be done in two main ways: extractive and abstractive. In extractive summarization, important sentences are directly selected from the original text, whereas in abstractive summarization, the system generates new sentences that summarize the text.
"""

# Preprocess the text: Tokenization and stopword removal
stop_words = set(stopwords.words('english'))
words = word_tokenize(text)
filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Convert sentences into a format suitable for TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(sentences)

# Calculate the importance score for each sentence
sentence_scores = np.sum(X.toarray(), axis=1)

# Get the indices of the top N sentences based on scores
top_n_sentences = np.argsort(sentence_scores)[-3:]  # Change '3' to desired number of sentences

# Sort the sentences in the order they appear in the text
top_n_sentences = sorted(top_n_sentences)

# Create the summary by combining the selected sentences
summary = ' '.join([sentences[i] for i in top_n_sentences])

# Print the original text and the generated summary
print("Original Text:\n", text)
print("\nSummarized Text:\n", summary)
