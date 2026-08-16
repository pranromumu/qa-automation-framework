from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    broweser = p.chromium.launch(headless=False)
    page = broweser.new_page()
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox_1=page.locator("input").nth(0)
    checkbox_2=page.locator("input").nth(1)
    checkbox_1.check()
    checkbox_2.uncheck()
    print("checkbox1:", checkbox_1.is_checked())
    print("chechbox2:", checkbox_2.is_checked())
    broweser.close()
