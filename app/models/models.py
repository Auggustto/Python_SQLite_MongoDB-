from db import db_pymongo
from datetime import datetime


class create_user:
    def __init__(self, name, cpf, address, type_account, agency, num_account):

        self.name = name
        self.cpf = cpf
        self.address = address
        self.type_account = type_account
        self.agency = agency
        self.num_account = num_account

    def create(self):
    
        post = {
            "name": self.name,
            "cpf": self.cpf,
            "address": self.address,
            "account": {
                "type": self.type_account,
                "agency": self.agency,
                "number": self.num_account
            },
            "date_time": datetime.utcnow()
        }

        try:
            # posts = db_pymongo.test_collection
            post_id = db_pymongo.collection.insert_one(post).inserted_id

            return f"User created sucessfully \n {post_id}"
        
        except Exception as e:
            
            return f"Error in creating user: {e}"
        
    def read_user():

        user = db_pymongo.db.posts.find_one()

        return user