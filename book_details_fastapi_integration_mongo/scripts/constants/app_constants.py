class APis:
    view_all_items_api = '/view_all'
    create_api = '/items/'
    update_api = '/items/{items_id}'
    delete_api = '/delete/{items_id}'
    send_email = '/send_email'
    get_api = '/billing-price'


class DBConstants:
    DB_URI = 'mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23'
    DB_NAME = 'interns_b2_23'
    DB_COllECTION = 'sonali_db_billing'


class Aggregation:
    aggr = [
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
    ]


class CommonConstants:
    APP_KEY = "main:app"
