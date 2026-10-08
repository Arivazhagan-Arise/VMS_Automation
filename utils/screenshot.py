from datetime import datetime
from pathlib import Path

def take_screenshot(driver, test_name):
    Path("screenshots").mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = Path("screenshots") / f"{test_name}_{timestamp}.png"
    driver.save_screenshot(str(path))
    return str(path)
