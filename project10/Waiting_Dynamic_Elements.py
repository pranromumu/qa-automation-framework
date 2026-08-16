

from playwright.sync_api import sync_playwright

with sync_playwright()  as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.locator("button").click()
    page.locator("#finish").wait_for(state="visible",timeout=10000)
    time= 10000
    text=page.locator("#finish").inner_text()
    assert "Hello World!" in text
    print(text)
    browser.close
