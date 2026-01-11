import re
import urllib.parse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Known Real News Sources
# -----------------------------
FACT_SOURCES = {
    "scientists confirm water on mars": "https://www.nasa.gov",
    "government launches new education policy": "https://www.india.gov.in",
    "india wins cricket world cup": "https://www.icc-cricket.com"
}

# -----------------------------
# Clean Text
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.strip()

# -----------------------------
# Simulated Search Results
# -----------------------------
def search_news(news):
    return [
        {"snippet": "Scientists have confirmed the presence of water on Mars"},
        {"snippet": "Water discovered on Mars by researchers"}
    ]

# -----------------------------
# Verify News
# -----------------------------
def verify_news(news):
    clean = clean_text(news)

    # Check known facts first
    if clean in FACT_SOURCES:
        return "TRUE", FACT_SOURCES[clean]

    results = search_news(news)

    if not results:
        return "FAKE", "https://www.google.com/search?q=" + urllib.parse.quote(news)

    corpus = [news] + [r["snippet"] for r in results]
    tfidf = TfidfVectorizer(stop_words="english").fit_transform(corpus)
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:]).max()

    if similarity > 0.25:
        return "TRUE", "https://www.google.com/search?q=" + urllib.parse.quote(news)
    else:
        return "FAKE", "https://www.google.com/search?q=" + urllib.parse.quote(news)

# -----------------------------
# MAIN PROGRAM (LOOP)
# -----------------------------
print("🔍 Fake News Detector (type 'exit' to quit)")

while True:
    user_news = input("\nEnter news text: ")

    if user_news.lower() == "exit":
        print("Program stopped.")
        break

    result, source = verify_news(user_news)

    print("Prediction:", "Real News" if result == "TRUE" else "Fake News")
    print("Reference:", source)
