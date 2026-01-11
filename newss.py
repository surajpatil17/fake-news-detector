import pandas as pd
import nltk
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('stopwords')
from nltk.corpus import stopwords

# Load dataset
df = pd.read_csv("new_with_evidence.csv")

# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return " ".join(words)

df['text'] = df['text'].apply(clean_text)

X = df['text']
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Vectorizer
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Fixed trusted links
REAL_NEWS_LINK = "https://www.reuters.com"
FAKE_NEWS_LINK = "https://factcheck.pib.gov.in"

# User input loop
while True:
    news = input("\nEnter news (type exit to stop): ")
    if news.lower() == "exit":
        break

    cleaned = clean_text(news)
    vec = vectorizer.transform([cleaned])
    result = model.predict(vec)[0]

    if result == 0:
        print("\n✅ REAL NEWS")
        print("🔗 Proof Link:", REAL_NEWS_LINK)
    else:
        print("\n❌ FAKE NEWS")
        print("🔗 Fact Check Link:", FAKE_NEWS_LINK)
