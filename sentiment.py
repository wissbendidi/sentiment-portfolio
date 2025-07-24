from textblob import TextBlob
import pandas as pd

def analyze_sentiment(csv_file):
    df = pd.read_csv(csv_file)
    df['sentiment'] = df['text'].apply(lambda text: TextBlob(text).sentiment.polarity)
    df.to_csv('tweets_with_sentiment.csv', index=False)
    print("Added sentiment scores and saved to tweets_with_sentiment.csv")
    return df

if __name__ == "__main__":
    analyze_sentiment('tweets.csv')
