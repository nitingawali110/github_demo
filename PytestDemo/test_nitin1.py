# Any pytest will start with test
#pytest methos names should start with test
# method name should Have Search
import pytest


@pytest.Mark.smoke
def test_firstprogram1():
    print("Hello")
    msg="Hello0"
    assert msg =="Hello","Test Failed beacause do not match"

def test_secondprogram2():
    print("Second,Hello")
