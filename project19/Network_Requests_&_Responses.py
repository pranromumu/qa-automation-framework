
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    with page.expect_response("**/") as response_info:
        page.reload()
    response = response_info.value
    print("Status:", response.status)
    print("URL:", response.url)
    assert response.status == 200
    print("✅ Network response verified!")
    browser.close()