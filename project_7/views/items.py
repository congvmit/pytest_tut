from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from models.items import Item
from schemas.items import CreateItem

router = APIRouter(prefix="/items", tags=["items"])


@router.post("")
async def create_item(item: CreateItem, session: AsyncSession = Depends(get_db)):
    try:
        new_item = Item(name=item.name, description=item.description, price=item.price)
        session.add(new_item)
        await session.commit()
    except Exception:
        return {"message": "internal error", "data": {}}
    else:
        return {
            "message": "success",
            "data": {
                "id": new_item.id,
                "name": new_item.name,
                "description": new_item.description,
                "price": new_item.price,
            },
        }


@router.get("/{id}")
async def get_item(id: str, session: AsyncSession = Depends(get_db)):
    try:
        item = await session.get(Item, id)
        if item is None:
            return {"message": "success", "data": {}}
        return {
            "message": "success",
            "data": {
                "id": item.id,
                "name": item.name,
                "description": item.description,
                "price": item.price,
            },
        }
    except Exception as e:
        return {"message": f"internal error {e}", "data": {}}
