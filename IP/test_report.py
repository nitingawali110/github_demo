# Certainly! Pytest provides various ways to generate reports for your test runs.
# Let's go through some common options using a simple example.
#
# Suppose you have a Python project with the following test file
# named `test_math_operations.py`:
#
# import pytest
#
# def test_addition():
#     assert 1 + 1 == 2
#
# def test_subtraction():
#     assert 3 - 1 == 2
#
# def test_multiplication():
#     assert 2 * 3 == 6
#
# def test_division():
#     assert 4 / 2 == 2

#
#
# Now, let's see how to generate different reports using Pytest.
#
# 1. **Default Console Output:**
#
#    When you run your tests using Pytest without any special flags or plugins,
#    it will display the test results directly in the console.
#    Open your terminal and navigate to the project directory, then run:
#
#    pytest test_math_operations.py
#
#
#    Pytest will execute your tests and display the results on the console,
#    indicating which tests passed and which failed.
#
# 2. **JUnit XML Report:**
#
#    You can generate JUnit-style XML reports, which are useful for integration with CI/CD systems.
#    To create a JUnit XML report, run the following command:
#
#
#    pytest --junitxml=report.xml test_math_operations.py
#    pytest --junitxml=report.xml test_report.py
#
#    This will create an XML report in a file called `report.xml` with the test results.
#
# 3. **HTML Report:**
#
#    To generate an HTML report that provides a more visually appealing
#    overview of your test results, you can use the `pytest-html` plugin. First,
#    you need to install it:
#
#    ```bash
#    pip install pytest-html
#    ```
#
#    Then, generate an HTML report like this:
#
#    ```bash
#    pytest --html=report.html test_math_operations.py
#    ```
#
#    This will create an HTML report in a file called `report.html`
#    that you can open in a web browser.
#
# 4. **Code Coverage Report:**
#
#    You can measure code coverage using a plugin like `pytest-cov`.
#    First, install it:
#
#    ```bash
#    pip install pytest-cov
#    ```
#
#    Then, run your tests with code coverage:
#
#    ```bash
#    pytest --cov=my_module test_math_operations.py
#    ```
#
#    Replace `my_module` with the name of the Python
#    module you want to measure coverage for. Pytest will
#    generate a coverage report, including which lines of code were executed during your tests.
#
# 5. **Custom Report Generation:**
#
#    If you need more customized reporting, you can
#    create your own custom report using Pytest hooks.
#    You can define custom hooks in your `conftest.py` file and
#    write code to generate reports in the format you desire.
#
# These are some of the common ways to generate reports
# using Pytest. Depending on your project and requirements,
# you can choose the reporting method that best suits your needs.




