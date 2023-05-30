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

    @staticmethod
    def excel_from_billing_data(self):
        """function to generate Excel sheet from billing data"""
        try:
            response_list = pipeline_aggregation(Aggregation.aggr)

            dataframe = pd.DataFrame(data=response_list)
            print(dataframe.shape)

            header = "XYZ Report"
            footer = "Overall Amount: {total_sum}".format(total_sum=dataframe["total_amount"].sum())
            writer = pd.ExcelWriter("report/billing_excel_record.xlsx", engine='xlsxwriter')
            dataframe.to_excel(writer, sheet_name="DATA_SHEET", header=True, index=False, startrow=1)
            workbook = writer.book
            worksheet = writer.sheets['DATA_SHEET']

            header_format1 = workbook.add_format({'bold': True,
                                                  'align': 'center',
                                                  'valign': 'vcenter',
                                                  'fg_color': '#D7E4BC',
                                                  'text_wrap': '1',
                                                  'font_size': '18',
                                                  'border': 1})

            footer_format1 = workbook.add_format({'bold': True,
                                                  'align': 'center',
                                                  'valign': 'vcenter',
                                                  'text_wrap': '1',
                                                  'font_size': '10',
                                                  'border': 1})

            worksheet.merge_range(0, 0, 0, len(dataframe.columns) - 1, header, header_format1)
            worksheet.merge_range(dataframe.shape[0] + 2,
                                  0,
                                  dataframe.shape[0] + 2,
                                  len(dataframe.columns) - 1,
                                  footer,
                                  footer_format1)
            writer.close()

            # Return the Excel file as a FileResponse
            return FileResponse("report/billing_excel_record.xlsx", filename="billing_excel_record.xlsx")
        except Exception as err:
            logger.error(ExcelHandlerException.EX018.format(error=str(err)))
