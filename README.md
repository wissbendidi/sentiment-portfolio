# 📊 Sentiment-Driven Crypto Portfolio Allocator

🚀 **Overview:**  
This project dynamically builds a hypothetical crypto portfolio allocation by:
- Fetching **live tweets** mentioning top cryptocurrencies (Bitcoin, Ethereum, etc.)
- Performing **sentiment analysis** using a pretrained NLP model (Hugging Face Transformers)
- Converting sentiment into portfolio weights
- Visualizing the allocation in an interactive pie chart

Built with Python, Plotly, and Transformers.  
*(Idea: catch market mood & reflect it in allocation!)*

---

## ✨ Features
✅ Live Twitter scraping with snscrape  
✅ NLP sentiment analysis (no API key needed)  
✅ Dynamic allocation using softmax  
✅ Beautiful interactive visualization (Plotly)  
✅ (Optional) Mini Streamlit app demo

---

## 🧰 Installation
Clone the repo:
```bash
git clone https://github.com/YourUsername/sentiment-portfolio.git
cd sentiment-portfolio
