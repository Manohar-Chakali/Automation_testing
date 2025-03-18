@REM pytest -s -v --html=reports/Automation_report2.html .\testCases

@REM pytest -s -v --alluredir="C:\Users\Lenovo\PycharmProjects\E-commersPorject\reports" .\testCases

pytest -s -v --alluredir="reports" --junitxml="reports/junit_report.xml" ".\testCases\Logout Test Cases" || exit 0
