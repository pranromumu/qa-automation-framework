from playwright.sync_api import sync_playwright
with sync_playwright()as p:
    browser= p.chromium.launch(headless=False)
    page= browser.new_page()
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    def handle_dialog(dialog):
        print("Alert says!", dialog.message)
        dialog.accept()
        #dialog.dismiss() # for challenge 3
    page.on("dialog",handle_dialog)
    page.locator("button").first.click()
    page.locator("button").nth(1).click() # challenge 1
    result= page.locator("#result").text_content()
    #assert "cancel" in result # challenge 2
    print("Result is !",result)
    browser.close()