from pprint import pprint
from pymongo import MongoClient, errors

client = MongoClient(host="mongodb://localhost:27017/", username="root", password="root")
db = client["nisitInfo"]
info_coll = db["info"]

for info in info_coll.find():
    pprint(info)

# info_coll.delete_many({})
