import pytest


@pytest.mark.asyncio
async def test_fixture(my_fixture):
    assert my_fixture == "Hello World"
