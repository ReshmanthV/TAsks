from scripts.schemas.gt_schema import Product
from scripts.db.mongo import CommonCollection


class GTHandler:
    def __init__(self):
        self.common = CommonCollection()

    async def get_list(self):
        """This function gives product list added"""
        err = {"message": "List is empty"}
        result = self.common.find({})
        final_result = []
        for each in result:
            final_result.append(each)
        try:
            if len(final_result) == 0:
                raise AttributeError
        except AttributeError:
            return err
        return {"Product list": final_result}

    def add_prod(self, product: Product):
        """This function adds items in grocery list."""
        err = {"message": "Item already exists"}
        result = self.common.find({})
        id_list = []
        for each in result:
            id_list.append(each["product_id"])
        if product.product_id in id_list:
            return err
        if product.product_amount <= 0 or product.quantity <= 0:
            err["message"] = "Amount/Quantity is invalid"
            return err
        self.common.insert_one(product.dict())
        err["message"] = "Product Added"
        return err

    def update_prod(self, prod_id: str, product: Product):
        """This is for updating the available product list"""
        err = {"message": "Item not in product list"}
        result = self.common.find({})
        id_list = []
        for each in result:
            id_list.append(each["product_id"])
        if prod_id not in id_list:
            return err
        if product.product_amount <= 0 or product.quantity <= 0:
            err["message"] = "Amount/Quantity is invalid"
            return err
        self.common.update_one({"product_id": prod_id}, product.dict())
        err["message"] = "Updated Successfully"
        return err

    def get_total(self):
        """This gives the total amount of items in product list"""
        amount_list = []
        result = self.common.find({})
        for each in result:
            amount_list.append(each["quantity"] * each["product_amount"])
        return {"Total amount": sum(amount_list)}

    def delete(self, prod_id: str):
        """This function deletes the product from product list"""
        result = self.common.find({})
        id_list = []
        for each in result:
            id_list.append(each["product_id"])
        if prod_id not in id_list:
            return {"message": "Product not found"}
        self.common.delete_one({"product_id": prod_id})
        return {"message": "Deleted Successfully"}
