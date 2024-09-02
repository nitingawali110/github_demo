# Parametrization in pytest allows you to run the same test function
# with multiple sets of input data, making it easier to test various scenarios
# and ensure that your code behaves correctly under different conditions.
# This is especially useful for data-driven testing.
# You can use the `@pytest.mark.parametrize` decorator to achieve parametrization.
#
# Here's an example of parametrization in pytest:
#
# Suppose you have a simple function that calculates the square of a number:
#
# ```python
def square(x):
    return x * x
# ```
#
# Now, you want to test this `square` function with multiple input-output pairs using parametrization in pytest.
#
# ```python
import pytest

# Define test data and expected results as tuples

test_data = [
    (2, 4),   # Test 1: input 2, expected output 4
    (3, 9),   # Test 2: input 3, expected output 9
    (4, 16),  # Test 3: input 4, expected output 16
]

# Create a parametrized test using the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("input_value, expected_result", test_data)

def test_square(input_value, expected_result):
    result = square(input_value)
    assert result == expected_result



# In this example:
#
# 1. We define a list called `test_data`,
# where each element is a tuple containing an input value and
# the expected output for a specific test case.
#
# 2. We use the `@pytest.mark.parametrize` decorator to create a
# parametrized test function called `test_square`.
# Inside the decorator, we specify the parameters we want to pass to the test function (`input_value` and `expected_result`)
# and provide the test data from `test_data`.
#
# 3. Inside the `test_square` function,
# pytest will automatically run the test for each set of input and
# expected output defined in `test_data`.
# For example, it will run the test with `input_value` 2
# and `expected_result` 4, and then with `input_value` 3 and `expected_result` 9.
#
# When you run this test suite using pytest,
# it will execute the `test_square` function three times,
# once for each set of test data.
# If any of the assertions fail,
# pytest will report which specific input values caused the failure.
#
# To run the parametrized test:
#
# ```bash
# pytest your_test_file.py
# ```
#
# This approach allows you to easily test your code against
# multiple test cases, improving code coverage and
# ensuring that your code handles various scenarios correctly.
