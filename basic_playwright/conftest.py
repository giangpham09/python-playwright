import pytest

@pytest.fixture
def setUp():
    print('Launch browser')
    print('Login')
    print('Browse products')

@pytest.fixture
def open_tab(setUp):
    print('open successful')