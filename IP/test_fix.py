import pytest


@pytest.fixture()
def setup():
    print("Launch Browser")
    print("Login")
    print("Browse Product")
    yield
    print("Logoff")
    print("Close Browser ")


def testadditemtocard(setup):
    print("Add item Sucessful")


def testremoveitemfromcart():
    print("Remove item Sucessful")

