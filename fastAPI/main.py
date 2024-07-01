from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str

items = []

@app.post("/add_items/", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@app.get("/list_items/", response_model=List[Item])
async def items_list():
    return items