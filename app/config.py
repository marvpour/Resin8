from decouple import config

API_KEY = config('API_KEY', default="", cast=str)
LLM_MODEL = config('LLM_MODEL', default="llama-3.1-sonar-small-128k-online", cast=str)
LLM_URL = "https://api.perplexity.ai/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
