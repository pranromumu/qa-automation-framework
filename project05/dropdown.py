
'''
from playwright.sync_api import sync_playwright
with sync_playwright()as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option("1")
    print("Select option 1")
    browser.close()
'''

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.mobiscroll.com/select/country-picker")
    page.locator(".mbsc-input-wrapper").first.click()
    page.locator("text=Malaysia").click()
    print("Malaysia")
    browser.close()
