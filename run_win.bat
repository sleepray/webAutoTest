python tools/clear_log.py

python tools/copy_history.py

pytest --alluredir allure-results

allure generate allure-results -c -o allure-report

allure open allure-report