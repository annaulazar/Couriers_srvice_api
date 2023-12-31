from datetime import datetime

from pydantic import BaseModel, Field, validator

from app.utils import validate_hours


class OrderDto(BaseModel):
    order_id: int
    weight: float
    regions: int
    delivery_hours: list[str]
    cost: int
    completed_time: datetime | None

    class Config:
        orm_mode = True


class CreateOrderDto(BaseModel):
    weight: float = Field(gt=0)
    regions: int = Field(gt=0)
    delivery_hours: list[str]
    cost: int = Field(ge=0)

    _validate_hours = validator('delivery_hours', allow_reuse=True)(validate_hours)


class CreateOrderRequest(BaseModel):
    orders: list[CreateOrderDto]


class GroupOrders(BaseModel):
    group_order_id: int
    orders: list[OrderDto]


class CouriersGroupOrders(BaseModel):
    courier_id: int
    orders: list[GroupOrders]


class CompleteOrder(BaseModel):
    courier_id: int
    order_id: int
    complete_time: datetime


class CompleteOrderRequestDto(BaseModel):
    complete_info: list[CompleteOrder]
