import pytest
import pytest_asyncio


@pytest_asyncio.fixture
def my_fixture():
    return "Hello World"
