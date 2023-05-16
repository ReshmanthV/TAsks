from pydantic import BaseModel


class Product(BaseModel):
    """This class is product details class"""
    product_id: str
    product_name: str
    product_amount: float
    quantity: int


class Email(BaseModel):
    receiver: str
