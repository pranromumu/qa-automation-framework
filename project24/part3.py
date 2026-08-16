
'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    def handle_request(request):
        print(
            "REQUEST:",
            request.method,
            request.url
        )
    def handle_response(response):
        print(
            "RESPONSE:",
            response.status,
            response.url
        )
    page.on("request", handle_request)
    page.on("response", handle_response)
    page.goto("https://the-internet.herokuapp.com/")
    browser.close()
'''


from playwright.sync_api import sync_playwright
with sync_playwright()as p:
    browser= p.chromium.launch(headless=False)
    page= browser.new_page()
    def hanlde_request(request):
        print("REQUEST:",request.method,request.url)
    def handle_response(resposne):
        print("RESPONSE:",resposne.status,resposne.url)
    page.on("request",hanlde_request)
    page.on("response",handle_response)
    page.goto("https://the-internet.herokuapp.com/")
    browser.close()