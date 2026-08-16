
'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # ==========================
    # API
    # ==========================
    request = p.request.new_context()
    response = request.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    api_data = response.json()
    print("API title:", api_data["title"])
    assert response.status == 200
    # ==========================
    # UI
    # ==========================
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    page_text = page.locator("body").inner_text()
    print("UI:", page_text)
    # ==========================
    # Integration verification
    # ==========================
    assert api_data["title"] in page_text
    print("🎉 API + UI verification passed!")
    browser.close()
    request.dispose()
'''
from playwright.sync_api import sync_playwright
with sync_playwright()as p:
    request = p.request.new_context()
    response = request.get(""https://jsonplaceholder.typicode.com/posts/1"")
    api_data = response.json
    print("API title:", api_data["title"])
    assert response.status == 200
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(""https://jsonplaceholder.typicode.com/posts/1"")
    text = page.locator("body").inner_text()
    print(text)
    assert api_data["title"] in text
    print("Done")
    browser.close()
    request.dispose()