# 🤖 LLM-Powered Product Data Augmentation & Enrichment Pipeline

Enhance product data in JSON files using real-time web scraping and Large Language Models (LLMs).

## 📌 Overview

This project enriches product information from JSON files by leveraging LLM APIs (e.g., Perplexity, OpenAI, Huggingface models) to gather up-to-date product details from the internet. The middleware processes each product object to augment descriptions, recommend prices, and add weight data dynamically.

## 🚀 Features
- **Real-Time Data Enrichment** – Uses LLMs to augment product descriptions, details, and taxonomy with fresh info scraped from the web.
- **Price Recommendation** – Automatically suggests prices when the price field is zero.
- **Product Weight Extraction** – Scrapes and appends product weight if available.
- **Dynamic Middleware** – Customizable LLM prompts to tailor augmentation and extraction.
- **Supports Multiple LLM APIs** – Easily switch between Perplexity, OpenAI, or open-source models.

## 🛠 How It Works
1. Upload a JSON file containing an array of product objects.
2. For each product, the middleware calls an LLM API with prompts built from existing fields (description, details, taxonomy).
3. The LLM fetches and returns enriched data added as an `augmented_data` field.
4. If the product price is zero, the LLM recommends a price to update the object.
5. The LLM attempts to find the product’s weight and appends it to `product_weight`.
6. Returns the augmented JSON file with enhanced product information.

## 📦 Installation

### Prerequisites
- Python 3.8+
- API Key for your chosen LLM service (e.g., Perplexity API key)

### Setup

1. Clone or download this repository.
2. Install the required packages:

```
pip install -r requirements.txt
```
3- Create a .env file in the project root with your API key:
```
API_KEY=<your_api_key_here>
```

## ▶️ Usage
1- Start the server:
```
uvicorn app.main:app --reload
```
2- Access the application at: 
```
http://localhost:8000
```
3- Upload your JSON file via the API or frontend interface to receive the augmented product data.

## 📚 Technologies Used
- **Python** – Core programming language
- **FastAPI** – API framework for serving the middleware
- **Uvicorn** – ASGI server for running FastAPI apps
- **Requests** – Handling HTTP requests
- **Python-dotenv** – Loading environment variables
- **Perplexity API** – Real-time data retrieval via LLM calls
- **Huggingface Transformers** – (Optional) Open-source LLM integration
- **LLama / OpenAI APIs** – Alternative LLM backends

