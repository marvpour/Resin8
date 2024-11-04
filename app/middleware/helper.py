import requests
import re
import json

from app.config import LLM_URL, HEADERS, LLM_MODEL


def remove_html_tags(text):
    clean_text = re.sub(r'<[^>]+>', '', text)
    return clean_text


def execute_llm(prompt):
    try:
        payload = {
            "model": LLM_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        response = requests.request("POST", LLM_URL, json=payload, headers=HEADERS)
        dict_response = json.loads(response.text)
        print(dict_response['choices'][0]['message']['content'])
        print('==============')
        return dict_response['choices'][0]['message']['content'].lower()
    except Exception as e:
        print(f'Error executing LLM. reason: {e}')
        return ""
