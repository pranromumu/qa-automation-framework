

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    # Add localStorage
    page.evaluate(
        "localStorage.setItem('user', 'Kabir')"
    )

    # Read localStorage
    value = page.evaluate(
        "localStorage.getItem('user')"
    )
    print("Stored user:", value)
    assert value == "Kabir"
    print("✅ localStorage verified!")
    browser.close()