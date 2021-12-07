from typing import List
from datetime import datetime as Datetime
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: float = 0.0

    class Config:
        orm_mode = True


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


class OrderDetailsBase(BaseModel):
    item_id: int
    quantity: int = 1

    class Config:
        orm_mode = True


class OrderDetails(OrderDetailsBase):
    order_id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    # user_id: int # Already in url path
    order_details: List[OrderDetailsBase]

    class Config:
        orm_mode = True


class Order(OrderBase):
    id: int
    user_id: int
    datetime: Datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    orders: List[Order] = []

    class Config:
        orm_mode = True
