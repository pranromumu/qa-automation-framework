from playwright.sync_api import sync_playwright

def verify_columns(page):
    text_a = page.locator("#column-a header").text_content()
    text_b = page.locator("#column-b header").text_content()

    print(f"Column A: {text_a}")
    print(f"Column B: {text_b}")

    return text_a, text_b


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/drag_and_drop")

    # Drag A → B
    source = page.locator("#column-a")
    target = page.locator("#column-b")

    source.drag_to(target)

    text_a, text_b = verify_columns(page)

    # Challenge 1
    print("Column A:", text_a)
    print("Column B:", text_b)

    # Challenge 2
    assert text_a == "B"
    assert text_b == "A"

    print("✅ A → B passed")

    # Challenge 3: Drag B → A
    source = page.locator("#column-b")
    target = page.locator("#column-a")

    source.drag_to(target)

    text_a, text_b = verify_columns(page)

    assert text_a == "A"
    assert text_b == "B"

    print("✅ B → A passed")

    # Challenge 4
    text_a, text_b = verify_columns(page)

    print("🎉 All challenges passed!")

    browser.close()