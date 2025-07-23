# Sentiment-Driven Crypto Portfolio Allocator

This project fetches live Twitter sentiment on top cryptocurrencies and dynamically allocates a hypothetical portfolio based on the sentiment scores. Built with Python, Transformers, and Plotly.

## 📊 What it does
- Scrape live tweets mentioning Bitcoin, Ethereum, etc.
- Analyze sentiment using pretrained NLP model
- Allocate portfolio weights dynamically
- Visualize as pie chart

## 🚀 How to run
```bash
pip install -r requirements.txt
jupyter notebook sentiment_portfolio.ipynb
