import requests
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("punkt")

# ---------------- CONFIG ----------------
NEWS_API_KEY = "PASTE_YOUR_NEWSAPI_KEY_HERE"
SIMILARITY_THRESHOLD = 0.25
# ---------------------------------------


def is_general_fact(text):
    keywords = ["is", "are", "capital", "population", "in india", "state"]
    text = text.lower()
    return any(word in text for word in keywords)


def fetch_real_news(query):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": "en",
        "pageSize": 5,
        "sortBy": "relevancy",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    if data.get("status") == "ok":
        for article in data.get("articles", []):
            if article.get("description"):
                articles.append(article["description"])

    return articles


def check_fake_news(user_news):

    if is_general_fact(user_news):
        return "ℹ️ Not a news statement (general fact)"

    real_articles = fetch_real_news(user_news)

    if not real_articles:
        return "❌ FAKE NEWS (No reliable sources found online)"

    corpus = [user_news] + real_articles
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(corpus)

    similarity = cosine_similarity(vectors[0:1], vectors[1:])[0]
    max_score = max(similarity)

    if max_score >= SIMILARITY_THRESHOLD:
        return f"✅ REAL NEWS (Similarity Score: {max_score:.2f})"
    else:
        return f"❌ FAKE NEWS (Similarity Score: {max_score:.2f})"


# ---------------- MAIN ----------------
if __name__ == "__main__":
    print("\n=== Fake News Detector ===\n")
    news = input("Enter news text:\n")

    result = check_fake_news(news)
    print("\nResult:", result)
