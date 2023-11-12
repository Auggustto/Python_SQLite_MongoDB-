from db import db_pymongo
from datetime import datetime


class create_user:
    def __init__(self, name, cpf, address, type_account, agency, num_accont):

        self.name = name
        self.cpf = cpf
        self.address = address
        self.type_account = type_account
        self.agency = agency
        self.num_accont = num_accont

    def create(self):
        
        post = [{
            "name": self.name,
            "cpf": self.cpf,
            "address": self.address},
            {            
            "type_account": self.type_account,
            "agency": self.agency,
            "num_accont": self.num_accont,
            "date_time": datetime.utcnow()
            }]
        
        posts = db_pymongo.db.posts
        post_id = posts.insert_one(post).inserted_id

        try:
            return post_id
        
        except Exception as e:
            
            return f"Error in creating user: {e}"