from scripts.core.db.mongo.interns_b2_23.sonali_db_billing.mongo_query import read_item, create_item, update_item, \
    delete_item, Item, pipeline_aggregation


class ItemHandler:

    def read_data(self):
        return read_item()

    def create_data(self, item: Item):
        return create_item(item)

    def update_data(self, item_id: int, item: Item):
        return update_item(item_id, item)

    def delete_data(self, item_id: int):
        return delete_item(item_id)

    def pipeline_aggregation(self):
        data = pipeline_aggregation([
            {
                '$addFields': {
                    'total_amount': {
                        '$multiply': [
                            '$quantity', '$cost'
                        ]
                    }
                }
            }, {
                '$group': {
                    '_id': None,
                    'total': {
                        '$sum': '$total_amount'
                    }
                }
            }, {
                '$project': {
                    '_id': 0
                }
            }
        ])
        print(data)
        return list(data)[0]['total']
