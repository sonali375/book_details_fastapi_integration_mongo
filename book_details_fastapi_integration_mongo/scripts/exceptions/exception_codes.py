"""classes to handle the Exceptions"""


class BillingHandlerException:
    EX001 = "Exception in read_data: {error}"
    EX002 = "Exception in create_data: {error}"
    EX003 = "Exception in update_data: {error}"
    EX004 = "Exception in delete_data: {error}"
    EX005 = "Exception in pipeline_aggregation: {error}"


class EmailHandlerException:
    EX006 = "Exception in send_email: {error}"


class BillingServicesException:
    EX007 = "Exception in view_all_items: {error}"
    EX008 = "Exception in create_item: {error}"
    EX009 = "Exception in update_item: {error}"
    EX010 = "Exception in delete_item: {error}"
    EX011 = "Exception in send_item: {error}"
    EX012 = "Exception in get_billing: {error}"
    EX019 = "Exception in get_excel_report: {error}"


class MongoQueryException:
    EX013 = "Exception in read_item: {error}"
    EX014 = "Exception in create_item: {error}"
    EX015 = "Exception in update_billing: {error}"
    EX016 = "Exception in delete_item: {error}"
    EX017 = "Exception in pipeline_aggregation: {error}"


class ExcelHandlerException:
    EX018 = "Exception in excel handling: {error}"
