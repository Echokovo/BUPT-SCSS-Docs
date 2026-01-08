import json
import os
import time
from openai import OpenAI
from config import wordbank_topics

template = """
请你围绕关键词{}，构建一个用于负面舆情发现的关键词表，长度为50个词，尽量避免重复。
请使用json作为返回格式，以下是一个模板：
{{
    "Keywords": {{
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    }}
}}
"""

def get_response(client: OpenAI, prompt):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature=1.5
    )
    return response.choices[0].message.content.strip("`json").strip()

def main(client, topic):
    response = get_response(client, template.format(topic))
    try:
        data = json.loads(response)
        with open(".\\Keywords\\" + topic + ".json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except json.decoder.JSONDecodeError:
        print("Error when decoding json")
        print(f"Topic: {topic}")
        print(f"Response: {response}")
    except Exception as e:
        print(e)
        print(f"Topic: {topic}")
        print(f"Response: {response}")

if __name__ == "__main__":
    os.makedirs(".\\Keywords", exist_ok=True)
    client = OpenAI(
        api_key="sk-256587d5388b4769ba6dc5cba76f42c4",
        base_url="https://api.deepseek.com",
    )
    for topic in wordbank_topics:
        main(client, topic)
        time.sleep(1)
    print("Success!")