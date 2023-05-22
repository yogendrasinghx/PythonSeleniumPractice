import pytest


@pytest.mark.usefixtures()
class TestExample:

    def test_editprofile(self, dataLoad):
        print(dataLoad['first_name'])
        print(dataLoad['last_name'])
        print(dataLoad['url'])

    def test_crossbrowser(self, crossBrowser):
        print(crossBrowser)