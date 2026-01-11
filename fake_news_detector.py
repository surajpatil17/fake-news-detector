import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# --------------------------------
# Try importing feedparser safely
# --------------------------------
try:
    import feedparser
    FEED_AVAILABLE = True
except ImportError:
    FEED_AVAILABLE = False
    print("⚠ feedparser not installed. Live news will be skipped.")

# --------------------------------
# 1️⃣ Load dataset
# --------------------------------
data = pd.read_csv("news_with_evidence.csv", on_bad_lines="skip")

X = data["text"]
y = data["label"]

# --------------------------------
# 2️⃣ Text Vectorization
# --------------------------------
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
X_features = vectorizer.fit_transform(X)

# --------------------------------
# 3️⃣ Train Model
# --------------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_features, y)

# --------------------------------
# 4️⃣ Evidence Dictionary
# --------------------------------
evidence_dict = dict(
    zip(
        data["text"],
        zip(data["evidence_link"], data["evidence_note"])
    )
)

# --------------------------------
# 5️⃣ Live News Prediction (Optional)
# --------------------------------
if FEED_AVAILABLE:
    print("\n🟢 LIVE NEWS PREDICTION RESULTS\n")

    rss = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(rss)
    headlines = [entry.title for entry in feed.entries[:10]]

    for i, headline in enumerate(headlines, start=1):
        vect = vectorizer.transform([headline])
        result = model.predict(vect)[0]

        status = "REAL 🟢" if result == 0 else "FAKE 🔴"
        print(f"{i}. {headline}")
        print(f"   ➤ Prediction: {status}")

        if headline in evidence_dict:
            link, note = evidence_dict[headline]
            print(f"   ➤ Evidence: {link}")
            print(f"   ➤ Reason: {note}")

        print()

# --------------------------------
# 6️⃣ Custom Statement Test
# --------------------------------
fake_examples = [
    "NASA confirmed the world will end tomorrow afternoon",
    "Newborn babies can now speak fluently from birth",
    "Government announces new scholarship program for students"
]

print("\n🛑 CUSTOM STATEMENT TEST\n")

for text in fake_examples:
    vect = vectorizer.transform([text])
    result = model.predict(vect)[0]
    status = "REAL 🟢" if result == 0 else "FAKE 🔴"

    print(f"Sentence: {text}")
    print(f"Prediction: {status}")

    if text in evidence_dict:
        link, note = evidence_dict[text]
        print(f"Evidence: {link}")
        print(f"Reason: {note}")

    print()
