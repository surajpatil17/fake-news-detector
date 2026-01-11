import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv(r"C:\Users\SURAJ MALIPATIL\OneDrive\Documents\PYTHON_PROGRAMS\movies.csv")


# Create a combined features column
# Handle missing columns by using fillna and available columns
df["combined"] = df.get("genre", "").fillna("") + " " + df.get("cast", "").fillna("") + " " + df.get("director", "").fillna("")

# Vectorize text
cv = CountVectorizer()
vector = cv.fit_transform(df["combined"])

# Calculate similarity
similarity = cosine_similarity(vector)

# Function to recommend movies
def recommend(movie_name):
    if "title" not in df.columns or movie_name not in df["title"].values:
        return ["Movie not found in database!"]
    index = df[df["title"] == movie_name].index[0]
    scores = list(enumerate(similarity[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    recommended = []
    for i in sorted_scores:
        recommended.append(df.iloc[i[0]]["title"])
    return recommended

# Test
movie = input("Enter movie name: ")
print("\nRecommended Movies:\n")
print(recommend(movie))
