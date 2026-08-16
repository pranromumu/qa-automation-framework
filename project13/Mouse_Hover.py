from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/hovers")
    profile= page.locator(".figure").first
    profile.hover()
    caption = page.locator(".figcaption").first
    text = caption.text_content()
    print(text)
    assert "user1" in text
    print("hover test passed")
    browser.close()