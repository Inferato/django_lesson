from django.urls import path
from ninja import NinjaAPI, Schema
from typing import List
from .models import Item

api = NinjaAPI()

class ItemSchemaIn(Schema):
    name: str
    description: str

class ItemSchemaOut(Schema):
    id: int
    name: str

class SingleItemSchema(ItemSchemaOut):
    description: str

@api.post("/items/", response=ItemSchemaOut)
def create_item(request, item: ItemSchemaIn):
    # new_item = Item.objects.create(**item.dict())
    # return new_item
    return item


@api.get("/items/", response=List[ItemSchemaOut])
def items_list(request):
    return list(Item.objects.all())


@api.get("/item/{item_id}/", response=SingleItemSchema)
def single_item(request, item_id: int):
    return Item.objects.get(id=item_id)
