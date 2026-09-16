# OpenCart E-Commerce Automation Framework

A production-style Selenium + Python test automation framework built on the
OpenCart e-commerce platform, demonstrating end-to-end UI automation with
the Page Object Model design pattern, data-driven testing, and Allure reporting.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test runner and fixture management |
| Page Object Model | Framework design pattern |
| Allure Reports | Test reporting and visualization |
| JSON / CSV | External test data management |
| GitHub | Version control and portfolio |

---

## Application Under Test

**OpenCart** — a full-featured e-commerce web application.  
URL: https://naveenautomationlabs.com/opencart/

Key modules covered:
- User Registration and Login
- Product Search and Navigation
- Shopping Cart and Checkout
- Wish List Management
- Account Management

---
## Framework Architecture
Automation_testing/
│
├── PageObjects/        # Page classes using POM pattern
│                       # Each page has locators + action methods
│
├── testCases/          # Test scripts using page objects
│                       # Organized by feature/module
│
├── testdata/           # External test data (JSON/CSV)
│                       # Enables data-driven testing
│
├── utilities/          # Reusable helper functions
│                       # Screenshot capture, wait strategies, etc.
│
├── Configurations/     # Environment config and base settings
│                       # Base URL, browser type, credentials
│
├── reports/            # Pytest HTML reports
├── allure-report/      # Allure visual reports
├── screenshots/        # Failure screenshots
│
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Project dependencies
├── run.bat             # One-click test execution script
└── Install_Packages.bat # Dependency installation script

---
##installation script
## Setup Instructions

### Prerequisites
- Python 3.8 or above
- Google Chrome (latest)
- pip package manager

### Installation

# Clone the repository
git clone https://github.com/Manohar-Chakali/Automation_testing.git
cd Automation_testing

# Install dependencies
pip install -r requirements.txt

##Or on Windows, simply run:
Install_Packages.bat

### Running Tests
#Run all tests
pytest testCases/ -v

#Run with HTML report
pytest testCases/ -v --html=reports/report.html
#Run with Allure report
pytest testCases/ --alluredir=allure-report
allure serve allure-report
#On Windows — one-click execution
run.bat

Key Framework Features
° Page Object Model — separates test logic from UI interaction,
making tests maintainable and reusable
° Data-Driven Testing — test data externalized to JSON/CSV files,
enabling multiple test scenarios from a single test script
° Allure Reporting — rich visual reports with test steps,
° screenshots on failure, and execution history
Screenshot Capture — automatic screenshot on test failure
for faster debugging
° Centralized Configuration — base URL and browser settings
managed in one place, no hardcoding in tests
° Reusable Utilities — common functions like waits and
screenshot helpers available across all test modules

Author
Manohar Chakali
Manual & Automation Test Engineer | 5 Years Experience
Bengaluru, India
GitHub: Manohar-Chakali
