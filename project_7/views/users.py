from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from models.users import User
from schemas.users import CreateUser

router = APIRouter(prefix="/users", tags=["users"])


@router.post("")
async def create_user(user: CreateUser, session: AsyncSession = Depends(get_db)):
    try:
        new_user = User(name=user.name, email=user.email, password=user.password)
        session.add(new_user)
        await session.commit()
    except Exception as e:
        return {"message": "internal error", "data": {}}
    else:
        return {
            "message": "success",
            "data": {
                "id": new_user.id,
                "name": new_user.name,
                "email": new_user.email,
            },
        }


@router.get("/{id}")
async def get_user_by_id(id: str, session: AsyncSession = Depends(get_db)):
    try:
        user = await session.get(User, id)
        if user is None:
            return {"message": "success", "data": {}}
        else:
            return {
                "message": "success",
                "data": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                },
            }
    except Exception as e:
        return {"message": f"internal error {e}", "data": {}}
