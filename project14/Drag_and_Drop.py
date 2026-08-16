

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    source = page.locator("#column-a")
    target = page.locator("#column-b")
    source.drag_to(target)
    text_a =page.locator("#column-a header").text_content()
    text_b = page.locator("#column-b header").text_content()
    print(text_a)
    print(text_b)
    print(f"Column A: {text_a}") # challenge 1
    print(f"Column B: {text_b}")
    assert text_a == "B" # challenge 2
    assert text_b == "A"

    assert text_a == "A"
    assert text_b == "B"
    print("swiped back") #Challenge 3
    browser.close()
    '''
    def verify_columns(page): # challenge 4
    text_a = page.locator("#column-a header").text_content()
    text_b = page.locator("#column-b header").text_content()
    print(f"Column A: {text_a}")
    print(f"Column B: {text_b}")
    '''