import pytest


@pytest.mark.smoke
def test_first_program():
    print("Hello")


@pytest.mark.skip
def test_grettingCreditCard():
    print("Good Morning")
