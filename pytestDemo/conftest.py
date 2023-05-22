import pytest


@pytest.fixture(scope='class')
def setup():
    print("I will execute first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return {'first_name': 'Yogendra', 'last_name': 'Singh', 'url': 'www.google.com'}

@pytest.fixture(params=['chrome','firefox','edge'])
def crossBrowser(request):
    return request.param