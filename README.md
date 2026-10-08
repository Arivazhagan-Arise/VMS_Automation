# VMS Automation Framework

Enterprise-style starter framework for VMS Web + Android APK + API + DB automation.

## Stack
- Python
- Pytest
- Selenium
- Appium
- Requests
- SQL/pyodbc
- Allure
- pytest-html

## Initial Web test

Activate virtual environment and install packages:

```powershell
pip install -r requirements.txt
```

Set credentials as environment variables instead of hard-coding passwords:

```powershell
$env:VMS_WEB_URL="https://stage-aicl-vms-ui.azurewebsites.net/"
$env:VMS_USERNAME="YOUR_USERNAME"
$env:VMS_PASSWORD="YOUR_PASSWORD"
```

Run:

```powershell
pytest
```

HTML report:

```text
reports/html/report.html
```

Allure results:

```text
reports/allure-results
```

Open Allure if the Allure CLI is installed:

```powershell
allure serve reports/allure-results
```

## Planned layers
Web -> Selenium
Mobile APK -> Appium
API -> Requests
Database -> pyodbc/SQL
E2E -> Web + Mobile + API + DB
