from selenium.webdriver.common.by import By
from core.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username = (By.XPATH, "//input[@id='UserId']")
        self.password = (By.XPATH, "//input[@id='password']")
        self.login_button = (By.XPATH, "//button[normalize-space()='Sign in']")
        self.dashboard = (By.XPATH, "//*[normalize-space()='Dashboard']")

    def login(self, username, password):
        self.enter_text(self.username, username)
        self.enter_text(self.password, password)
        self.click(self.login_button)

    def is_dashboard_displayed(self):
        return self.is_displayed(self.dashboard)
