import pytest

@pytest.fixture()
def setup():
    print("\nbefore testing")
    yield
    print("\ntake screen picture")
    print("take logs file")


def test_demo_1():
    assert 1 == 1

def test_demo_2(setup):
    print("testing")
    assert 2 > 1

