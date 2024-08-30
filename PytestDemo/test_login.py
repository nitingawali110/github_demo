# Pytest framwork
import pytest


@pytest.fixture
def setup():
    print("Launch Browser")
    print("Login")
    print("Browse Product")
    yield
    print("Logoff")
    print("close Browser")

def testlogin(setup):
    print("Login Sucessful")

def  testLogoff(setup):
    print("Logoff Sucessful")

def testcalculation():
    assert 2+2==4
