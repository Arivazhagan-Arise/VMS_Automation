import os
import allure
from pages.web.login_page import LoginPage

@allure.feature("Login")
@allure.story("Valid Login")
@allure.title("Verify valid VMS login")
def test_valid_login(driver):
    driver.get(os.getenv("VMS_WEB_URL", "https://stage-aicl-vms-ui.azurewebsites.net/"))
    login_page = LoginPage(driver)
    login_page.login(
        os.getenv("VMS_USERNAME", "AICL1087"),
        os.getenv("VMS_PASSWORD", "Arise@123")
    )
    assert login_page.is_dashboard_displayed()
