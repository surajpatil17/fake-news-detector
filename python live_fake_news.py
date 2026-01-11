import feedparser
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ---------------------------------
# 1️⃣ Load training dataset
# ---------------------------------
data = pd.read_csv("news.csv")   # CSV must contain: text,label
x = data["text"]
y = data["label"]

# Convert text → numeric TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
x_features = vectorizer.fit_transform(x)

# Train ML model
model = LogisticRegression()
model.fit(x_features, y)

# ---------------------------------
# 2️⃣ Fetch Live Google News
# ---------------------------------
feed_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
feed = feedparser.parse(feed_url)
articles = [entry.title for entry in feed.entries]

# ---------------------------------
# 3️⃣ Predict & Print Results
# ---------------------------------
print("\n🟢 LIVE NEWS PREDICTION RESULTS\n")

for i, headline in enumerate(articles[:10]):   # Show top 10 news
    vect = vectorizer.transform([headline])
    result = model.predict(vect)[0]
    status = "REAL 🟢" if result == 0 else "FAKE 🔴"

    print(f"{i+1}. {headline}")
    print(f"   ➤ Prediction: {status}\n")
