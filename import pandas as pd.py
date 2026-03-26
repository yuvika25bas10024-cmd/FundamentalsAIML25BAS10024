import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

data = {
    'text': [
        'Get a free iPhone now!', 'Hey, are we still meeting for lunch?',
        'Congratulations! You won a lottery.', 'Can you send me the report by EOD?',
        'Urgent: Your bank account is suspended. Click here.', 'Dinner at 7 PM tonight?'
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}
df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")

new_emails = ["Win a million dollars today!", "Is the meeting still on?"]
new_emails_vectorized = vectorizer.transform(new_emails)
print(f"Predictions: {model.predict(new_emails_vectorized)}")
