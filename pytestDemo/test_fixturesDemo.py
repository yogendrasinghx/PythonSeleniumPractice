import pytest


@pytest.fixture()
def setup():
    print("I will run first")
    yield
    print("I will run last")


def test_fixureDemo(setup):
    print("I will run in the middle")