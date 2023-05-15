from fastapi import APIRouter
from scripts.core.db.mongo.interns_b2_23.sonali_db_billing.mongo_query import Item
from scripts.core.handlers.billing_handler import ItemHandler
from scripts.core.handlers.email_handler import send_email, Email

item_router = APIRouter()


@item_router.get("/")
def view_all_items():
    item_object = ItemHandler()
    return item_object.read_data()


@item_router.post("/items/")
def create_item(item: Item):
    item_object = ItemHandler()
    return item_object.create_data(item)


@item_router.put("/items/{items_id}")
def update_item(item_id: int, item: Item):
    item_object = ItemHandler()
    return item_object.update_data(item_id, item)


@item_router.delete("/delete/{items_id}/")
def delete_item(item_id: int):
    item_object = ItemHandler()
    return item_object.delete_data(item_id)


@item_router.post("/send_email")
def send_item(email: Email):
    item_handler = ItemHandler()
    result = item_handler.pipeline_aggregation()
    message = f"total amount is {result}"
    send_email(message, email)
    return {"message": "email sent"}


@item_router.get("/billing-price")
def get_billing():
    item_handler = ItemHandler()
    result = item_handler.pipeline_aggregation()
    return result
