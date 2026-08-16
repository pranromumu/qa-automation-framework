
'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request = p.request.new_context()
    response = request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data={
            "title": "QA Automation",
            "body": "API + UI Testing",
            "userId": 1
        }
    )
    print("Status:", response.status)
    data = response.json()
    print(data)
    assert response.status == 201
    assert data["title"] == "QA Automation"
    print("✅ API creation successful!")
    request.dispose()
'''

from playwright.sync_api import sync_playwright
with sync_playwright()as p:
    request = p.request.new_context()
    response = request.post(
        "https://jsonplaceholder.typicode.com/posts"
        data={
            "title": "QA Automation"
            "body" : "API + UI Testing"
            "userId": 1
        }
    )
    print("Status:",response.status)
    data= response.json
    print(data)
    assert response.status == 201
    assert data("title") == "QA Automation"
    print("done")
    request.dispose