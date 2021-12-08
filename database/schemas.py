from typing import List, Optional
from datetime import datetime as Datetime
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: float = 0.0
    image_id: int

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
    # item_id: int # Already in url path
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
    username: str
    email: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    disabled: Optional[bool] = False

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    username: Optional[str] = None

    class Config:
        orm_mode = True
