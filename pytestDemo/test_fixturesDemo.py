import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixureDemo1(self):
        print("I will run in the middle")

    def test_fixureDemo2(self):
        print("I will run in the middle")

    def test_fixureDemo3(self):
        print("I will run in the middle")

    def test_fixureDemo4(self):
        print("I will run in the middle")
