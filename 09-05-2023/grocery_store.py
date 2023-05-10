"""This a grocery list program using FastAPI"""

from fastapi import FastAPI
from pydantic import BaseModel


class Product(BaseModel):
    """This class is product details class"""
    product_name: str
    product_amount: float
    quantity: int


app = FastAPI()

product_list = {}


@app.get("/prod_list")
async def get_list():
    """This function gives product list added"""
    if len(product_list) == 0:
        return "Product list is empty"
    return {"Product list": product_list}


@app.post("/add_prod/{prod_id}")
def add_prod(prod_id: str, product: Product):
    """This function adds items in grocery list."""
    if prod_id in product_list:
        return "Item already exists"
    if product.product_amount <= 0 or product.quantity <= 0:
        return "Amount/Quantity is invalid"
    product_list[prod_id] = product.dict()
    return {"Products": product_list}


@app.put("/update_prod/{prod_id}")
def update_prod(prod_id: str, product: Product):
    """This is for updating the available product list"""
    if prod_id not in product_list:
        return "Product not found"
    if product.product_amount <= 0 or product.quantity <= 0:
        return "Amount/Quantity is invalid"
    product_list.update({
        prod_id: product.dict()
    })
    return "Updated Successfully"


@app.get("/total_amount")
def get_total():
    """This gives the total amount of items in product list"""
    amount_list = []
    for prod_id in product_list.keys():
        amount_list.append(product_list[prod_id]["product_amount"] * product_list[prod_id]["quantity"])
    return {"Total amount": sum(amount_list)}


@app.delete("/del_prod/{prod_id}")
def delete(prod_id: str):
    """This function deletes the product from product list"""
    if prod_id not in product_list:
        return "Product not found"
    del product_list[prod_id]
    return "Deleted Successfully"
