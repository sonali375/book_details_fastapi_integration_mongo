"""importing constants"""
from scripts.constants.app_constants import DBConstants, Aggregation
from scripts.core.db.mongo.interns_b2_23.sonali_db_billing.mongo_query import Item, pipeline_aggregation
from scripts.utility.mongo_utility import MongoCollectionBaseClass, MongoConnect
from scripts.exceptions.exception_codes import *
from scripts.logging.logger import logger


class ItemHandler:
    """
    class to handle the items in mongo
    """

    def __init__(self):
        self.user_mongo_obj = MongoCollectionBaseClass(database=DBConstants.DB_NAME,
                                                       mongo_client=MongoConnect(DBConstants.DB_URI).client,
                                                       collection=DBConstants.DB_COllECTION)

    def read_data(self):
        """Function to read data"""
        try:
            logger.info("Handler: read_data")
            res = self.user_mongo_obj.find({})
            # res= 'success'
            if res:
                logger.info("read_data: Records Read Successfully")
                return list(res)
        except Exception as err:
            logger.error(BillingHandlerException.EX001.format(error=str(err)))
            return {"status": "failed"}
            # return read_item()

    def create_data(self, item: Item):
        """Function to create data"""
        try:
            logger.info("Handler: create_data")
            res = self.user_mongo_obj.insert_one(data=item.dict())
            # res= 'success'
            if res:
                logger.info("create_data: Record Created Successfully")
                return {"status": "success"}
        except Exception as err:
            logger.error(BillingHandlerException.EX002.format(error=str(err)))
            return {"status": "failed"}
            # return create_item(item)

    def update_data(self, item_id: int, item: Item):
        """Function to update data"""
        try:
            logger.info("Handler: update_data")
            res = self.user_mongo_obj.update_one({"id": item_id}, item.dict())
            # res= 'success'
            if res:
                logger.info("update_data: Record Updated Successfully")
                return {"status": "success"}
        except Exception as err:
            logger.error(BillingHandlerException.EX003.format(error=str(err)))
            return {"status": "failed"}
            # return update_item(item_id, item)

    def delete_data(self, item_id: int):
        """Function to delete data"""
        try:
            logger.info("Handler: delete_data")
            res = self.user_mongo_obj.delete_one({'id': item_id})
            # res= 'success'
            if res:
                logger.info("delete_data: Record Deleted Successfully")
                return {"status": "success"}
        except Exception as err:
            logger.error(BillingHandlerException.EX004.format(error=str(err)))
            return {"status": "failed"}
        # return delete_item(item_id)

    def pipeline_aggregation(self):
        """Function to aggregate data"""
        try:
            logger.info("Handler: pipeline_aggregation")
            data = pipeline_aggregation(Aggregation.aggr)
            logger.info("pipeline_aggregation:", data)
        except Exception as err:
            logger.error(BillingHandlerException.EX005.format(error=str(err)))

        return list(data)[0]['total']
