import pytest
import pytest_asyncio
from asyncmock import AsyncMock
from cat_fact import CatFact


@pytest_asyncio.fixture
async def cat_fact():
    return CatFact()


# Test with real HTTP call
@pytest.mark.asyncio
async def test_cat_fact(cat_fact):
    fact = await cat_fact.get_fact()
    assert fact["status"] == 200
    assert "data" in fact["result"]


# Test with mock HTTP call
@pytest.mark.asyncio
async def test_get_cat_fact_mocked(mocker):
    mock_resp = {"status": 200, "result": {"data": "Cats are awesome!"}}
    mocker.patch.object(CatFact, "get_fact", new=AsyncMock(return_value=mock_resp))

    cat_fact_instance = CatFact()
    result = await cat_fact_instance.get_fact()
    assert result["status"] == 200
    assert "data" in result["result"]
    assert result["result"]["data"] == "Cats are awesome!"
