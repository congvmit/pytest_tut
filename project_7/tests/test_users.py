import pytest


@pytest.mark.asyncio
async def test_create_user(client):
    response = client.post(
        "/users",
        json={"name": "user1", "email": "email1", "password": "password1"},
    )
    user_id = response.json()["data"]["id"]
    print("user_id", user_id)
    assert response.status_code == 200
    assert response.json() == {
        "message": "success",
        "data": {"id": user_id, "name": "user1", "email": "email1"},
    }


@pytest.mark.asyncio
async def test_get_user_found(client):
    response = client.post(
        "/users",
        json={"name": "user2", "email": "email2", "password": "password2"},
    )
    user_id = response.json()["data"]["id"]
    print("user_id", user_id)
    response = client.get(f"/users/{user_id}")
    # print(response.json())
    assert response.status_code == 200
    assert response.json() == {
        "message": "success",
        "data": {"id": user_id, "name": "user2", "email": "email2"},
    }


@pytest.mark.asyncio
async def test_get_user_not_found(client):
    response = client.get("/users/3")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {
        "message": "success",
        "data": {},
    }

    