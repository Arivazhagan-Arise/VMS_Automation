import pytest
import allure
from core.driver_factory import WebDriverFactory
from utils.screenshot import take_screenshot

@pytest.fixture
def driver():
    driver = WebDriverFactory.create_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            path = take_screenshot(driver, item.name)
            with open(path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
