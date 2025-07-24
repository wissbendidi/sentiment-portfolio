import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweets(query, limit=100):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= limit:
            break
        tweets.append([tweet.date, tweet.content])
    df = pd.DataFrame(tweets, columns=['date', 'text'])
    df.to_csv('tweets.csv', index=False)
    print(f"Scraped {len(df)} tweets and saved to tweets.csv")
    return df

if __name__ == "__main__":
    scrape_tweets("bitcoin")
