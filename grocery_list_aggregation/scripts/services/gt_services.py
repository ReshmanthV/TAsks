from fastapi import APIRouter
from scripts.api import EndPoints
from scripts.core.handlers.gt_handlers import GTHandler
from scripts.core.handlers.mail_handler import send_mail
from scripts.schemas.gt_schema import Product, Email

gt_router = APIRouter()


@gt_router.get(EndPoints.get_list)
async def get_list():
    try:
        gt_handler = GTHandler()
        final_list = await gt_handler.get_list()
        return final_list
    except Exception as e:
        return str(e)


@gt_router.post(EndPoints.add_prod)
def add_prod(product: Product):
    try:
        gt_handler = GTHandler()
        return gt_handler.add_prod(product)
    except Exception as e:
        return str(e)


@gt_router.put(EndPoints.update_prod)
def update_prod(prod_id: str, product: Product):
    try:
        gt_handler = GTHandler()
        return gt_handler.update_prod(prod_id, product)
    except Exception as e:
        return str(e)


@gt_router.delete(EndPoints.del_prod)
def delete(prod_id: str):
    try:
        gt_handler = GTHandler()
        return gt_handler.delete(prod_id)
    except Exception as e:
        return str(e)


@gt_router.get(EndPoints.total_amount)
def get_total():
    try:
        gt_handler = GTHandler()
        return gt_handler.get_total()
    except Exception as e:
        return str(e)


@gt_router.post(EndPoints.email)
def send_email(email: Email):
    try:
        return send_mail(email)
    except Exception as e:
        return str(e)
