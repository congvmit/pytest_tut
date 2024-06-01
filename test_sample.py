import pytest


def test_awesomeness():
    assert True


@pytest.mark.xfail(reason="always failing test")
def test_failing():
    assert False


# Fixtures: To explicitly provide a dependency to a
# test function, we can use fixtures.
@pytest.fixture
def example_fixture():
    return 1


def test_with_fixture(example_fixture):
    assert example_fixture == 1
