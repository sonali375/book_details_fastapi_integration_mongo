from pymongo import MongoClient

client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")

db = client.interns_b2_23
Item = {"id": int,
        "name": str,
        "quantity": int,
        "cost": int
        }

billing = db.sonali_db_billing
billing.insert_one(Item)
