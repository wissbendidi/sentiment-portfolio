from scraper import scrape_tweets
from sentiment import analyze_sentiment
from visualize import plot_sentiment_histogram
from portfolio import mock_portfolio

def main():
    print("Starting sentiment portfolio analysis...")
    scrape_tweets("bitcoin", limit=100)
    analyze_sentiment('tweets.csv')
    plot_sentiment_histogram('tweets_with_sentiment.csv')
    mock_portfolio()
    print("Done!")

if __name__ == "__main__":
    main()
