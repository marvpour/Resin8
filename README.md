# Problem Statement

You will be provided with a JSON file along with this code. Upon uploading the JSON file, the middleware simply returns the file. Your task is to write code in the middleware file (`processPrompt`) that uses publicly available LLM APIs (e.g., LLama, OpenAI, or other open-source models like those from Huggingface.io) to perform the following:

### 1. For each JSON object in the array:
   - Use the `description`, `product details`, and `taxonomy` fields to gather more information about that product from the internet.
   - Enhance the object by adding more detailed information in a new field called `"augmented_data"`.

### 2. This `"augmented_data"` field should:
   - Contain data that improves on the existing information under the fields `description`, `product details`, or `taxonomy`.

### 3. This workflow should dynamically scrape data from the internet about the described product in real-time.

## Optional Features:

### 4. If the `price` field of a product object is `0`:
   - Scrape the data from the internet and provide a price recommendation.
   - If a price suggestion is found, write it into the `price` field.

### 5. If possible, find the product's weight and:
   - Add it to a new field called `"product_weight"`.

---

# Proposed Solution

## LLM API
I am using Perplexity API to get the latest info about given products. To test the application, you can set the `API_KEY` in the `.env` file and that should enable the LLM call.
Reason for choosing Perplexity API is retrieving information from the latest data found online, which is the purpose of this problem as I understand it.

## Prompts
I designed two different LLM calls, one for `augmented_data` field and one for `price` and `weight` fields.
Default prompt defined in the script for each call should give us a clear response, but as in LLM's nature, it may function 100% of times as expected.

## Price and Weight
To solve this, I forced the LLM to respond in a specific format, so that I can get the data easier. The `price` field will be there if found, or `priceUSD` is `0`.
Product weight is also included if it is found and not empty.

---

## How to Run the application on Mac

- Install requirements using:
    `pip install -r requirements.txt`
- Add API Key to the `.env` file:
    `API_KEY=<you api key>`
- Run the application using:
  `uvicorn app.main:app --reload`
- Use the application with calling:
    `http://localhost:8000`