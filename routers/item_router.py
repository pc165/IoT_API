from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database.dal import DAL, get_dal
import database.schemas as schemas
import database.models as models

item_router = APIRouter()


@item_router.post("/items/{item_id}", response_model=schemas.Item)
async def create_item(item: schemas.ItemBase, db: DAL = Depends(get_dal)):
    return await db.create_user_item(item=item)


@item_router.get("/items/", response_model=List[schemas.Item])
async def get_all_items(skip: int = 0, limit: int = 100, db: DAL = Depends(get_dal)) -> List[models.Items]:
    items = await db.get_items(skip=skip, limit=limit)
    return items
