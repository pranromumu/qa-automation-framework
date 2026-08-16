

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/tables")
    rows= page.locator("#table1 tbody tr")
    print("Total rows:", rows.count())
    for i in range(rows.count()):
        row= rows.nth(i)
        print(row.text_content())
        print(row.first.text_content())
    email = page.locator("#table1 tbody tr td:nth-child(3)")
    for i in range(email.count()):
        print(email.nth(i).text_content())
    word= page.locator("#table1").inner_text()
    assert "jsmith@gmail.com" in word
    print("correct")
    browser.close()
