import pytest


@pytest.mark.smoke
def test_first_program():
    greet = "Hello"
    assert greet == "Hi", "String does not matched"


@pytest.mark.xfail
def test_secondCreditCard():
    a = 3
    b = 6
    assert a + 3 == b, "Addition does not matched"
