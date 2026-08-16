from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    request = p.request.new_context()
    response = request.get(
        "https://httpbin.org/response-headers?Content-Type=application/json"
    )
    print("Status:", response.status)
    print("Headers:")
    print(response.headers)
    request.dispose()