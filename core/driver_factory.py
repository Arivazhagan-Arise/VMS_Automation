from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebDriverFactory:
    @staticmethod
    def create_driver():
        options = Options()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)
