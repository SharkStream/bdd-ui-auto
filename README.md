# auto_ui

## Run this demo
```shell
pip install -r requirements.txt
python run_tests.py --tags @UI
```

## Use allure to view the reports
```shell
allure serve reports/allure-results
```

## Examples
```shell
python run_tests.py                              # Run with default settings
python run_tests.py --headless                   # Run in headless mode
python run_tests.py --browser firefox            # Run with Firefox
python run_tests.py --browser webkit --headless  # Run WebKit in headless mode
python run_tests.py --parallel                   # Run tests in parallel
python run_tests.py --parallel --headless        # Run parallel tests in headless mode
python run_tests.py --parallel --workers 7       # Run with 7 parallel workers
python run_tests.py --tags @smoke                # Run only smoke tests
python run_tests.py --tags @smoke @regression    # Run smoke and regression tests
python run_tests.py --serve-report               # Serve Allure report after tests
python run_tests.py --tracing                    # Enable Playwright tracing, video recording
```