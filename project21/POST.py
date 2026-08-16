'''
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    request = p.request.new_context()
    response = request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data={
            "title": "My QA Test",
            "body": "Learning API testing",
            "userId": 1
        }
    )

    print("Status:", response.status)
    data = response.json()
    print("Response:", data)
    assert response.status == 201
    assert data["title"] == "My QA Test"
    assert data["userId"] == 1
    print("✅ POST passed!")
    request.dispose()
'''

from playwright.sync_api import sync_playwright
with sync_playwright()as p:
    request= p.request.new_context()
    response = request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data={
            "title": "My QA Test",
            "body": "Learninf API testing",
            "userId": 1
        }
    )
    print("Status:",response.status)
    data = response.json()
    print("Response", data)
    assert response.status == 201
    assert data["title"] == "My QA Test"
    assert data["userId"] == 1   
    print("test passed!")
    request.dispose()