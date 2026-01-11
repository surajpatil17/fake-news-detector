# =========================
# 1. Import Libraries
# =========================
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# =========================
# 2. Sample Training Data
# (0 = Real, 1 = Fake)
# =========================
news_data = [
    "Government launches new education policy",
    "Scientists discover new planet",
    "Celebrity claims aliens landed in village",
    "Drinking salt water cures all diseases",
    "Election commission announces polling dates",
    "Fake miracle medicine spreads online"
]

labels = [0, 0, 1, 1, 0, 1]

# =========================
# 3. Text Preprocessing
# =========================
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

news_data = [clean_text(text) for text in news_data]

# =========================
# 4. Feature Extraction
# =========================
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(news_data)

# =========================
# 5. Train Model
# =========================
model = LogisticRegression()
model.fit(X, labels)

# =========================
# 6. Prediction Function
# =========================
def detect_fake_news(news):
    news = clean_text(news)
    vector = vectorizer.transform([news])
    prediction = model.predict(vector)

    if prediction[0] == 1:
        return "❌ Fake News"
    else:
        return "✅ Real News"

# =========================
# 7. User Input
# =========================
user_news = input("Enter news text: ")
result = detect_fake_news(user_news)
print("Prediction:", result)
