import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# 1. Load reviews
df = pd.read_csv("reviews.csv")

# 2. Analyze sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["review"].apply(get_sentiment)
df["Score"] = df["review"].apply(lambda x: round(TextBlob(x).sentiment.polarity, 2))

# 3. Show results
print("\n===== SENTIMENT ANALYSIS RESULTS =====")
print(df[["review", "Sentiment", "Score"]])

# 4. Count each sentiment
counts = df["Sentiment"].value_counts()
print("\n===== SUMMARY =====")
print(counts)

# 5. Create pie chart
colors = ["#2ecc71", "#e74c3c", "#f39c12"]
plt.figure(figsize=(7, 7))
plt.pie(counts, labels=counts.index, colors=colors, autopct="%1.1f%%", startangle=140)
plt.title("Sentiment Analysis of Customer Reviews", fontsize=14, fontweight="bold")
plt.savefig("output_chart.png")
plt.show()
print("\nChart saved as output_chart.png")