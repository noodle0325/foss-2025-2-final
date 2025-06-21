import os
import requests

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def create_page(title, content):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name": {
                "title": [{"text": {"content": title}}]
            }
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "text": [{"type": "text", "text": {"content": content[:2000]}}]
                }
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code, response.text)

if __name__ == "__main__":
    with open("docs/기능정리.md", "r", encoding="utf-8") as f:
        content = f.read()
    create_page("기능 정리 자동 등록", content)
