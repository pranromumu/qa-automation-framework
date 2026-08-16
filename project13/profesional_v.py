from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/hovers")
    profiles = page.locator(".figure")
    for i in range(profiles.count()):
        profile = profiles.nth(i)
        profile.hover()
        caption = page.locator(".figcaption").nth(i)
        text = caption.inner_text()
        print(text)
        expected_user = f"user{i+1}"
        assert expected_user in text
        link = caption.locator("a")
        assert link.is_visible()
        print(f"✅ {expected_user} verified")

    browser.close()