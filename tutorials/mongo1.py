from pprint import pprint
from pymongo import MongoClient, errors
from bson import json_util
import json

# DOMAIN = '172.25.0.5'
# PORT = 27017

# try: 
#     client = MongoClient(
#         host = [ str(DOMAIN) + ":" + str(PORT)],
#         serverSelectionTimeoutMS = 3000,
#         username = "root",
#         password = "root"
#     )

#     print("server version: ", client.server_info()["version"])

#     database_names = client.list_database_names()

# except errors.ServerSelectionTimeoutError as err:
#     client = None
#     database_names = []

#     print("pymongo ERROR: ", err)

# print("\ndatabases: ", database_names)

client = MongoClient(host="mongodb://localhost:27017/", username="root", password="root")
db = client["customersdb"]
customers = db["customers"]

pprint(client.list_database_names())

# for customer in customers.find():
#     pprint(customer)

a = customers.find_one({"name": "Sandy"})

s = json.loads(json_util.dumps(a))

print(s)

customers.update_one(filter={
    'name':'Sandy'
    }, update={'$set': {'address':'Beach'}})

for customer in customers.find({"name": "Sandy"}):
    print(customer)    

# for customer in customers.find({"name": "S"}):
    # print(isinstance(customer, None))

# customers_list = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
# x = customers.insert_many(customers_list)
# # print list of the _id values of the inserted documents:
# print(x.inserted_ids)
