# Problem Statement

You will be provided with a JSON file along with this code. Upon uploading the JSON file, the middleware simply returns the file. Your task is to write code in the middleware file (`processPrompt`) that uses publicly available LLM APIs (e.g., LLama, OpenAI, or other open-source models like those from Huggingface.io) to perform the following:

### 1. For each JSON object in the array:
   - Use the `description`, `product details`, and `taxonomy` fields to gather more information about that product from the internet.
   - Enhance the object by adding more detailed information in a new field called `"augmented_data"`.

### 2. This `"augmented_data"` field should:
   - Contain data that improves on the existing information under the fields `description`, `product details`, or `taxonomy`.

### 3. This workflow should dynamically scrape data from the internet about the described product in real-time.

---

## Optional Features:

### 4. If the `price` field of a product object is `0`:
   - Scrape the data from the internet and provide a price recommendation.
   - If a price suggestion is found, write it into the `price` field.

### 5. If possible, find the product's weight and:
   - Add it to a new field called `"product_weight"`.

# FastAPI Application

This is a FastAPI application that demonstrates basic usage.

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/OAkinbode/ProductAugApp.git
cd ProductAugApp

```

### 2. Install all dependencies using either of the following:

pip install -r requirements.txt

or

pip3 install -r requirements.txt

### 3. Run the application using for mac

uvicorn app.main:app --reload

### 3. Run the application using for windows

python.exe -m uvicorn.main app.main:app --reload

### 4. Use application in browser

visit http://localhost:8000