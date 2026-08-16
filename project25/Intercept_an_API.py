
'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    def handle_route(route):
        print("Intercepted:", route.request.url)
        route.continue_()
    page.route(
        "https://jsonplaceholder.typicode.com/posts/1",
        handle_route
    )
    page.goto(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    browser.close()
'''    
from playwright.sync_api import sync_playwright
with sync_playwright()as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    def handle_route(route):
        print("Intercepted", route.request.url)
        route.continue_()
    page.route("https://jsonplaceholder.typicode.com/posts/1", handle_route)
    page.goto("https://jsonplaceholder.typicode.com/posts/1")
    browser.close()