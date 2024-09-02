# Certainly! Let's explore fixtures with a basic example in Python using the popular testing framework pytest. In this example, we'll create test fixtures to set up test data, initialize objects, and demonstrate how fixtures enhance modularity.
#
# Suppose you have a simple calculator application with two functions: addition and subtraction. We want to write test cases for these functions using fixtures.
#
# ```python
# calculator.py - The code to be tested

# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b


# Now, let's write test cases using pytest and fixtures:
#
# ```python
# test_calculator.py - The test cases using fixtures

import pytest
from calculator import add, subtract

# Define a fixture to set up common data or objects
@pytest.fixture
def numbers():
    a = 10
    b = 5
    return a, b

# Test case 1: Testing the addition function
def test_addition(numbers):
    a, b = numbers
    result = add(a, b)
    assert result == 15

# Test case 2: Testing the subtraction function
def test_subtraction(numbers):
    a, b = numbers
    result = subtract(a, b)
    assert result == 5


# In this example:
#
# 1. We have a `calculator.py` module with two simple functions,
# `add` and `subtract`, which perform addition and subtraction operations.
#
# 2. We create a test module named `test_calculator.py` to write test cases for these functions.
#
# 3. We define a fixture called `numbers`.
# This fixture sets up common data (two numbers, in this case)
# that will be used by multiple test cases. The fixture returns these numbers as a tuple.
#
# 4. The `test_addition` and `test_subtraction` test cases
# both accept the `numbers` fixture as an argument.
# This means that the `numbers` fixture will run before these test cases, providing them with the necessary data.
#
# 5. In the test cases, we perform addition and
# subtraction operations using the provided numbers
# and then use assertions to verify that the results match our expectations.
#
# By using fixtures in this way:
#
# - We ensure that the setup (in this case, providing the numbers)
# is consistent across multiple test cases.
# If we need to change the numbers or add more test cases, we only need to update the fixture in one place.
#
# - We promote modularity by separating the test data setup from the test logic,
# making the code more maintainable.
#
# - We can easily reuse fixtures in other test cases,
# allowing us to create a library of reusable setup code for different parts of our application.
#
# Overall, fixtures help create a clean and organized
# structure for your tests, making it easier to maintain and extend your test suite as your project grows.
