
import pytest


# Marking Tests:
#
# You can mark tests using the @pytest.mark decorator.
# Marks are used to categorize tests and perform actions or filtering based on these marks.


@pytest.mark.smoke
def test_smoke_test_1():
    assert True

@pytest.mark.smoke
def test_smoke_test_2():
    assert True

@pytest.mark.slow
def test_slow_test():
    assert True


@pytest.mark.smoke  # Marking a test as a smoke test
def test_login():
    # Test logic here
    assert True

@pytest.mark.regression  # Marking a test as a regression test
def test_data_processing():
    # Test logic here
    assert True


# pytest -k smoke  # Runs tests marked as smoke
# pytest -k regression  # Runs tests marked as regression


@pytest.mark.skip(reason="Test not ready yet")
def test_feature_in_progress():
    # Test logic here
    assert True

# @pytest.mark.skipif(condition,reason="Condition not met")
# def test_conditionally_skipped():
#     # Test logic here


# The @pytest.mark.skip decorator skips the test unconditionally,
# while @pytest.mark.skipif skips the test if a specified condition is met.
