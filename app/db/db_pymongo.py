import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://leonardoaugusto1000a:i61kzEujOia3uiFb@pymongo.d9mv3aq.mongodb.net/?retryWrites=true&w=majority")

db = client.clent_test

collection = db.test_collection

# print(db.list_collection_names())