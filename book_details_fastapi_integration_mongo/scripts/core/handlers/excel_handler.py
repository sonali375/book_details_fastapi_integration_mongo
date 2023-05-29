import pandas as pd
from scripts.utility.mongo_utility import MongoCollectionBaseClass
from scripts.logging.logger import logger
from fastapi import FastAPI
from fastapi.responses import FileResponse
from scripts.core.handlers.billing_handler import pipeline_aggregation
from scripts.exceptions.exception_codes import ExcelHandlerException
from scripts.constants.app_constants import Aggregation

app = FastAPI()


class ExcelGeneration:
    """class for generating excel"""

    def __init__(self):
        self.mongo_obj = MongoCollectionBaseClass()

    def excel_from_billing_data(self):
        """function to generate Excel sheet from billing data"""
        try:
            logger.info("Handler:excel_from_billing_data")
            # Fetching the data for the Excel file
            excel_data = pipeline_aggregation(Aggregation.aggr)
            # overall_total = sum(row['total_amount'] for row in excel_data)
            # overall_total_row = {'overall_total': overall_total}
            # excel_data.append(overall_total_row)
            print(excel_data)

            # Create a DataFrame from the data
            df = pd.DataFrame(excel_data)

            # Create the Excel file
            excel_file = 'report/billing_excel_record.xlsx'
            df.to_excel(excel_file, index=False)

            # Return the Excel file as a FileResponse
            return FileResponse(excel_file,
                                media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                filename='report/billing_excel_record.xlsx')
        except Exception as err:
            logger.error(ExcelHandlerException.EX018.format(error=str(err)))
