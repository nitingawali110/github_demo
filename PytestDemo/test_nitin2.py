# Any pytest will start with test
#pytest methos names should start with test
# method name should Have Search
# You can Mark(Tag) tests @pytest.mark.smoke and then run with -m

import pytest


@pytest.mark.smoke
def test_smoke1():
    print("Hello")


def test_secondprogram2():
    print("Second,Hello")
