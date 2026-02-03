import allure
from playwright.sync_api import sync_playwright

@allure.title("Verify login functionality")
@allure.feature("Authentication")
def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://fovero.app/")

        page.get_by_role("button", name="Sign in").click()

        page.get_by_role("textbox", name="Email").fill("dhruvil.patel@concettolabs.com")
        page.get_by_role("textbox", name="Email").press("Tab")

        page.get_by_role("textbox", name="Password").fill("Devil@123")
        page.get_by_role("button", name="Sign in").click()

        page.get_by_role("button", name="Dhruvil Patel").click()
        page.get_by_role("button", name="Logout Logout").click()

        context.close()
        browser.close()
