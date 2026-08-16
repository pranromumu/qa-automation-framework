

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    context.add_cookies([
        {
            "name": "username",
            "value": "Kabir",
            "domain": "the-internet.herokuapp.com",
            "path": "/"
        }
    ])
    cookies = context.cookies()
    print(cookies)
    browser.close()