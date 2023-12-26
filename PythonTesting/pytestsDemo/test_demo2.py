# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in a method
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_first_program():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do mot match"

def test_second_programCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition matches"


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")