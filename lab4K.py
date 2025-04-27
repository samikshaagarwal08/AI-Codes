import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Example text for sentiment analysis
text = "I love this product! It's absolutely amazing and works perfectly."

# Get sentiment scores
sentiment_scores = sia.polarity_scores(text)

# Output the sentiment scores
print("Sentiment Scores:", sentiment_scores)

# Analyze overall sentiment
if sentiment_scores['compound'] >= 0.05:
    print("Sentiment: Positive")
elif sentiment_scores['compound'] <= -0.05:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
