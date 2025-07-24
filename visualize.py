import pandas as pd
import matplotlib.pyplot as plt

def plot_sentiment_histogram(csv_file):
    df = pd.read_csv(csv_file)
    plt.figure(figsize=(8, 5))
    plt.hist(df['sentiment'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Sentiment distribution')
    plt.xlabel('Sentiment polarity')
    plt.ylabel('Frequency')
    plt.savefig('sentiment_histogram.png')
    plt.show()
    print("Histogram saved as sentiment_histogram.png")

if __name__ == "__main__":
    plot_sentiment_histogram('tweets_with_sentiment.csv')
