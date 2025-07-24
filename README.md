# Sentiment-Driven Crypto Portfolio

This project demonstrates how to leverage social media sentiment from Twitter to inform cryptocurrency portfolio insights. It scrapes live tweets about Bitcoin, analyzes their sentiment using natural language processing, visualizes the sentiment distribution, and connects this data to a mock crypto portfolio.

---

## Features

- **Twitter scraping** using [`snscrape`](https://github.com/JustAnotherArchivist/snscrape) (no API keys required)
- **Sentiment analysis** with [`TextBlob`](https://textblob.readthedocs.io/en/dev/) to determine tweet polarity
- **Data visualization** with `matplotlib` to plot sentiment score distributions
- **Simulated cryptocurrency portfolio** representing holdings and current prices
- Interactive Jupyter Notebook to explore data and workflow step-by-step

---

## Project Structure

├── .gitignore
├── app.py # Main script to run all steps sequentially
├── portfolio.py # Mock portfolio data and functions
├── requirements.txt # Python dependencies
├── scraper.py # Twitter scraping functionality
├── sentiment.py # Sentiment analysis processing
├── sentiment_portfolio.ipynb # Interactive notebook for exploration
└── visualize.py # Visualization of sentiment data


---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/sentiment_portfolio.git
cd sentiment_portfolio
```

    Create and activate a Python virtual environment:
```
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# OR on Windows
venv\Scripts\activate

    Install required packages:

pip install -r requirements.txt
```
Usage
Run the full pipeline

To run scraping, sentiment analysis, visualization, and portfolio display in one go:
```
python app.py
```
Explore interactively

Open the Jupyter Notebook to run and tweak each step interactively:
```
jupyter notebook sentiment_portfolio.ipynb
```
How It Works

    Scraping (scraper.py): Fetches recent tweets mentioning "bitcoin" using snscrape.

    Sentiment Analysis (sentiment.py): Uses TextBlob to calculate polarity scores (-1 to 1) for each tweet.

    Visualization (visualize.py): Plots a histogram showing how many tweets are positive, neutral, or negative.

    Portfolio Simulation (portfolio.py): Contains example cryptocurrency holdings and prices.

    Main Script (app.py): Coordinates the entire process.

Limitations

    Sentiment analysis is basic and may not reflect true market sentiment.

    Twitter scraping depends on site structure and can break if Twitter changes its layout.

    Portfolio is static and for demonstration only; no real trading or price updates.

    This project is educational and not financial advice.

Dependencies

    snscrape

    pandas

    textblob

    matplotlib

    jupyter (for the notebook)

License

This project is licensed under the MIT License.
Author

wissal bendidi — 
GitHub: wissbendidi
