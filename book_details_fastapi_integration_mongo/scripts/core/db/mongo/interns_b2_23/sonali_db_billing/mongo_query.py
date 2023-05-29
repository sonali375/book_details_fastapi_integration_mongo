"""importing MongoClient for connection"""
from fastapi import FastAPI
from pymongo import MongoClient

from scripts.constants.app_constants import DBConstants
from scripts.core.schema.model import Item
from scripts.exceptions.exception_codes import MongoQueryException
from scripts.logging.logger import logger

app = FastAPI()

# Creating instance of mongo client
client = MongoClient(DBConstants.DB_URI)
# Creating database
db = client[DBConstants.DB_NAME]
# # Creating document
billing = db[DBConstants.DB_COLLECTION]


def read_item():
    """Function to read the items"""
    logger.info("Mono_Query: read_item")
    data = []
    try:
        for items in billing.find():
            del items['_id']
            data.append(items)
    except Exception as err:
        logger.error(MongoQueryException.EX013.format(error=str(err)))
    return {
        "db": data
    }


def create_item(item: Item):
    """Function to create the items"""
    try:
        logger.info("Mono_Query: create_item")
        billing.insert_one(item.dict())
        db[item.id] = item.name
    except Exception as err:
        logger.error(MongoQueryException.EX014.format(error=str(err)))
    return {
        "db": db
    }


def update_item(item_id: int, item: Item):
    """Function to update the items"""
    try:
        logger.info("Mono_Query: update_item")
        billing.update_one({"id": item_id}, {"$set": item.dict()})
    except Exception as err:
        logger.error(MongoQueryException.EX015.format(error=str(err)))


def delete_item(item_id: int):
    """Function to delete the items"""
    try:
        logger.info("Mono_Query: delete_item")
        billing.delete_one({"id": item_id})
    except Exception as err:
        logger.error(MongoQueryException.EX016.format(error=str(err)))
    return {"message": "deleted"}


def pipeline_aggregation(pipeline: list):
    """Function to aggregate the items"""
    try:
        logger.info("Mono_Query: pipeline_aggregation")
        print(pipeline)
        return billing.aggregate(pipeline)
    except Exception as err:
        logger.error(MongoQueryException.EX017.format(error=str(err)))
