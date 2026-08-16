

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    request = p.request.new_context()
    response = request.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        data={
            "id": 1,
        "title": "Updated QA Test",
        "body": "Updated content",
        "userId": 1
        }
    )
    print("Status",response.status)
    data = response.json()
    assert response.status == 200
    assert data["title"] == "Updated QA Test"
    assert data["userId"] == 1
    print("Update passed")
    request.dispose