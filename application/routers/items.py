from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/items", tags=["items"])


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


# Sample data
items_db = []


@router.get("/", response_model=List[Item])
async def get_items():
    return items_db


@router.post("/", response_model=Item)
async def create_item(item: Item):
    items_db.append(item)
    return item


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = next((item for item in items_db if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
