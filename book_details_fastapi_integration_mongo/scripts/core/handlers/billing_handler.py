import scripts.constants.app_constants
from scripts.constants.app_constants import DBConstants, Aggregation
from scripts.core.db.mongo.interns_b2_23.sonali_db_billing.mongo_query import read_item, create_item, update_item, \
    delete_item, Item, pipeline_aggregation
from scripts.utility.mongo_utility import MongoCollectionBaseClass, MongoConnect
from scripts.exceptions.exception_codes import *
import logging as log


class ItemHandler:

    def __init__(self):
        self.user_mongo_obj = MongoCollectionBaseClass(database=DBConstants.DB_NAME,
                                                       mongo_client=MongoConnect(DBConstants.DB_URI).client,
                                                       collection=DBConstants.DB_COllECTION)

    def read_data(self):
        res = self.user_mongo_obj.find({})
        # res= 'success'
        if res:
            return {"status": "success", "message": "Showing all records"}
        else:
            return {"status": "failed", "message": "Error showing records", "error": ""}
        # return read_item()

    def create_data(self, item: Item):
        res = self.user_mongo_obj.insert_one(data=item.dict())
        # res= 'success'
        if res:
            return {"status": "success", "message": "Record Inserted"}
        else:
            return {"status": "failed", "message": "Error inserting", "error": ""}
        # return create_item(item)

    def update_data(self, item_id: int, item: Item):
        res = self.user_mongo_obj.update_one({"id": item_id}, item.dict())
        # res= 'success'
        if res:
            return {"status": "success", "message": "Record Updated"}
        else:
            return {"status": "failed", "message": "Error updating", "error": ""}
        # return update_item(item_id, item)

    def delete_data(self, item_id: int):
        res = self.user_mongo_obj.delete_one({'id': item_id})
        # res= 'success'
        if res:
            return {"status": "success", "message": "Record Deleted"}
        else:
            return {"status": "failed", "message": "Error deleting", "error": ""}
        # return delete_item(item_id)

    def pipeline_aggregation(self):
        data = pipeline_aggregation(Aggregation.aggr)
        print(data)
        return {"total_amount": list(data)[0]['total']}
