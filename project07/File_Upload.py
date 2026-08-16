from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")
    page.locator("#file-upload").set_input_files(r"D:\QA-Automation\project07\test.txt")
    page.locator("#file-submit").click()
    message = page.locator("h3").text_content()
    assert "File Uploaded" in message
    print("passed")
    uploaded_filename= page.locator("#uploaded-file").text_content()
    print(uploaded_filename)
    assert "test.txt" in uploaded_filename
    print("passed file name verified!")
    
    browser.close()