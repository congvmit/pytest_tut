import pytest


@pytest.mark.asyncio
async def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_create_item(client):
    response = client.post(
        "/items",
        json={"name": "item1", "description": "description1", "price": 9.99},
    )
    item_id = response.json()["data"]["id"]
    assert response.status_code == 200
    assert response.json() == {
        "message": "success",
        "data": {
            "id": item_id,
            "name": "item1",
            "description": "description1",
            "price": 9.99,
        },
    }


@pytest.mark.asyncio
async def test_get_item_found(client):
    response = client.post(
        "/items",
        json={"name": "item2", "description": "description2", "price": 9.99},
    )
    item_id = response.json()["data"]["id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {
        "message": "success",
        "data": {
            "id": item_id,
            "name": "item2",
            "description": "description2",
            "price": 9.99,
        },
    }


@pytest.mark.asyncio
async def test_get_item_not_found(client):
    response = client.get("/items/3")
    # print(response.json())
    assert response.status_code == 200
    assert response.json() == {
        "message": "success",
        "data": {},
    }
