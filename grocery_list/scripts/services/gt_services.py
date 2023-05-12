from fastapi import APIRouter

from scripts.api import EndPoints
from scripts.core.handlers.gt_handlers import GTHandler
from scripts.schemas.gt_schema import Product

gt_router = APIRouter()


@gt_router.get(EndPoints.get_list)
async def get_list():
    gt_handler = GTHandler()
    final_list = await gt_handler.get_list()
    return final_list


@gt_router.post(EndPoints.add_prod)
def add_prod(product: Product):
    gt_handler = GTHandler()
    return gt_handler.add_prod(product)


@gt_router.put(EndPoints.update_prod)
def update_prod(prod_id: str, product: Product):
    gt_handler = GTHandler()
    return gt_handler.update_prod(prod_id, product)


@gt_router.delete(EndPoints.del_prod)
def delete(prod_id: str):
    gt_handler = GTHandler()
    return gt_handler.delete(prod_id)


@gt_router.get(EndPoints.total_amount)
def get_total():
    gt_handler = GTHandler()
    return gt_handler.get_total()
