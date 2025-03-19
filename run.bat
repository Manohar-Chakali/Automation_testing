@REM pytest -s -v --html=reports/Automation_report2.html .\testCases

@REM pytest -s -v --alluredir="C:\Users\Lenovo\PycharmProjects\E-commersPorject\reports" .\testCases

@REM pytest -s -v --alluredir="C:/Users/Lenovo/PycharmProjects/E-commersPorject/reports" --junitxml="C:/Users/Lenovo/PycharmProjects/E-commersPorject/reports/junit_report.xml" ".\testCases\Logout Test Cases" || exit 0

@REM pytest --junitxml=reports/junit_report.xml --alluredir=reports/allure ".\testCases\Logout Test Cases\test_TC_LG_004.py" || exit 0

pytest -m "not (navigation or negative)" ".\testCases" --junitxml=reports/junit_report.xml --alluredir=reports/allure --clean-alluredir || exit 0


