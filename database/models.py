from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from .config import Base
from sqlalchemy.sql import func


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String)
    # one user can have multiple orders
    orders = relationship("Orders", cascade="all, delete", lazy='selectin')


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    datetime = Column(DateTime(timezone=True), server_default=func.now())
    # orders can have multiple items
    order_details = relationship("OrderDetails", cascade="all, delete", lazy='selectin')


# association table to store extra data
class OrderDetails(Base):
    __tablename__ = "order_details"
    order_id = Column(Integer, ForeignKey("orders.id"), primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"), primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    items = relationship("Items", lazy='selectin')


class Items(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    price = Column(Float, index=True, nullable=False)
