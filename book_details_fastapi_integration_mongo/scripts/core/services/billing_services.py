"""importing APIRouter"""
from fastapi import APIRouter
from scripts.core.db.mongo.interns_b2_23.sonali_db_billing.mongo_query import Item
from scripts.core.handlers.billing_handler import ItemHandler
from scripts.core.handlers.email_handler import send_email, Email
from scripts.constants.app_constants import APis
from scripts.exceptions.exception_codes import BillingServicesException
from scripts.logging.logger import logger
from json2html import *

item_router = APIRouter()


@item_router.get(APis.view_all_items_api)
def view_all_items():
    """Function to view all items"""
    result_dict = {"status": "failed", "data": None}
    try:
        logger.info("Services: view_all_items")
        item_object = ItemHandler()
        result_dict = {"status": "success", "data": item_object.read_data()}
    except Exception as err:
        logger.error(BillingServicesException.EX007.format(error=str(err)))
    return result_dict


@item_router.post(APis.create_api)
def create_item(item: Item):
    """Function to create items"""
    try:
        logger.info("Services: create_item")
        item_object = ItemHandler()
        return item_object.create_data(item)
    except Exception as err:
        logger.error(BillingServicesException.EX008.format(error=str(err)))


@item_router.put(APis.update_api)
def update_item(item_id: int, item: Item):
    """Function to update items"""
    try:
        logger.info("Services: update_item")
        item_object = ItemHandler()
        return item_object.update_data(item_id, item)
    except Exception as err:
        logger.error(BillingServicesException.EX009.format(error=str(err)))


@item_router.delete(APis.delete_api)
def delete_item(item_id: int):
    """Function to delete items"""
    try:
        logger.info("Services: delete_item")
        item_object = ItemHandler()
        return item_object.delete_data(item_id)
    except Exception as err:
        logger.error(BillingServicesException.EX010.format(error=str(err)))


@item_router.post(APis.send_email)
def send_item(email: Email):
    """Function to send items"""
    try:
        item_object = ItemHandler()
        all_billing_list_json = item_object.read_data()
        table = json2html.convert(json=all_billing_list_json)
        logger.info("Services: send_item")
        item_handler = ItemHandler()
        result = item_handler.pipeline_aggregation()
        message1 = f"Please find the table as shown below: {table}"
        message2 = f"{message1} \n total amount is {result}"
        send_email(message2, email)
        logger.info("send_item: Email sent successfully")
        return {"message": "email sent"}
    except Exception as err:
        logger.error(BillingServicesException.EX011.format(error=str(err)))
        return {"Error": err.args}


@item_router.get(APis.get_api)
def get_billing():
    """Function to get the billing"""
    try:
        logger.info("Services: get_billing")
        item_handler = ItemHandler()
        result = item_handler.pipeline_aggregation()
        return result
    except Exception as err:
        logger.error(BillingServicesException.EX012.format(error=str(err)))
