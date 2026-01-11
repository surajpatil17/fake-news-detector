import requests

API_KEY = "PASTE_YOUR_REAL_API_KEY_HERE"
API_URL = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

def check_news(news_text):
    params = {
        "query": news_text,
        "key": API_KEY
    }

    response = requests.get(API_URL, params=params)

    if response.status_code != 200:
        print("❌ API ERROR:", response.status_code)
        print("Details:", response.text)
        return

    data = response.json()

    if "claims" not in data or len(data["claims"]) == 0:
        print("\n🟡 RESULT: NO FACT-CHECK FOUND")
        print("ℹ️ This news is not verified by any fact-check website.\n")
        return

    claim = data["claims"][0]
    review = claim["claimReview"][0]

    verdict = review.get("textualRating", "Unknown")
    source = review.get("publisher", {}).get("name", "Unknown")
    link = review.get("url", "N/A")

    print("\n📰 NEWS:", news_text)
    print("✅ VERDICT:", verdict)
    print("🔎 SOURCE :", source)
    print("🌐 LINK   :", link)
    print("-" * 60)


# --------------------------------
# USER INPUT LOOP
# --------------------------------
print("\n🔍 FAKE NEWS DETECTION USING FACT-CHECK API")
print("Type 'exit' to stop\n")

while True:
    news = input("Enter News: ")

    if news.lower() == "exit":
        print("👋 Exiting...")
        break

    check_news(news)
