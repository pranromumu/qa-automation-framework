from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    response = page.goto(
        "https://jsonplaceholder.typicode.com/posts/1")
    print("Status:", response.status)
    data = response.json()
    print("Data:", data)
    print("User ID:", data["userId"])
    print("Post ID:", data["id"])
    assert response.status == 200
    assert data["userId"] == 1
    assert data["id"] == 1
    print("✅ API response verified!")
    browser.close()