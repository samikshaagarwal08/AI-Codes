import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Example of a more extensive dataset
data = {'text': ['Breaking news: Stocks are soaring.', 'Fake news: The moon is made of cheese.',
                 'Real news: Scientists discovered a new species.', 'Fake news: Aliens landed.',
                 'Breaking: New technology revolutionizes life.', 'Breaking news: New discovery in physics.',
                 'Fake news: You can lose 10 kg in 2 days!', 'Real news: Government plans new education policy.',
                 'Breaking: Earthquake hits city center.', 'Fake news: Earth is flat.'],
        'label': ['real', 'fake', 'real', 'fake', 'real', 'real', 'fake', 'real', 'real', 'fake']}
df = pd.DataFrame(data)

# Stratified train-test split
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42, stratify=df['label'])

# Vectorization and training
vectorizer = TfidfVectorizer(stop_words='english')  # Use 'english' directly
X_train_tfidf = vectorizer.fit_transform(X_train)
model = MultinomialNB().fit(X_train_tfidf, y_train)

# Evaluation
y_pred = model.predict(vectorizer.transform(X_test))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nReport:\n", classification_report(y_test, y_pred))

# Test with new data
test_news = ["Breaking: The new iPhone feature is amazing."]
print("Prediction:", model.predict(vectorizer.transform(test_news))[0])
