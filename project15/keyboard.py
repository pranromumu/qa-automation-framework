

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/key_presses")
    page.locator("body").click()
    page.keyboard.press("A")
    result = page.locator("#result").text_content()
    print("Result:", result)
    assert "A" in result
    print("Keyboard test passed")
    browser.close()