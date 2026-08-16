'''
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    request = p.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    print("Status:", response.status)
    data = response.json()
    print("Post ID:", data["id"])
    print("User ID:", data["userId"])
    assert response.status == 200
    assert data["id"] == 1
    print("✅ GET passed!")
    request.dispose()
'''
from playwright.sync_api import sync_playwright
with sync_playwright()as p:
    request = p.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    print("Status:",response.status)
    data=response.json()
    print("Post ID:",data["id"])
    print("User ID:",["userId"])
    assert response.status == 200
    assert data["id"] == 1
    print("Get Passed")
    request.dispose()
