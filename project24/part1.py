
'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    def handle_request(request):
        print("REQUEST:", request.method, request.url)
    page.on("request", handle_request)
    page.goto("https://the-internet.herokuapp.com/")
    browser.close()
'''
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    def handle_request(request):
        print("request:",request.method ,request.url) 
    page.on("request",handle_request)
    page.goto =("https://the-internet.herokuapp.com/")
    browser.close()

