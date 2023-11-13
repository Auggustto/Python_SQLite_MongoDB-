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
        


    def read_user(cpf):

        user = db_pymongo.collection.find_one({"cpf":cpf})
        # print("Read user", user)
        
        if user != None:
            return user
        
        else:
            return f"Invalid CPF error or user has been deleted."
    
    def delete_user(cpf):
        id_user = create_user.read_user(cpf)

        if id_user:
            user_id = id_user['_id']

            try:
                convert_id = {'_id': db_pymongo.ObjectId(user_id)}

                result = db_pymongo.collection.delete_one(convert_id)

                if result.deleted_count == 1:
                    
                    return f"User with CPF {cpf} deleted successfully."

            except Exception as e:
                return f"Error in delete user -> {e}"
            
        else:
            return f"No user found with CPF {cpf}."


    def update_client(cpf):

        address = input("Insert address: \n")
        type_account = input("Input type account \n")

        if type_account == '':
            type_account = "Basic"

        values = {
            "address": address,
            "account": {
                "type_account": type_account
            }}
        
        try:
            filter_cpf = {"cpf": cpf}

            result = db_pymongo.collection.update_one(filter_cpf, {"$set": {"address": address, "account.type": type_account}})

            if result.modified_count == 1:
                return f"User with CPF {cpf} updated successfully."
            
            else:
                return f"No user found with CPF {cpf}."
            
        except Exception as e:
            return f"Error in update user -> {e}"

    def read_all_users():

        try:
            all_users = db_pymongo.collection.find()

            return all_users

        except Exception as e:
            print(f"Error in reading users -> {e}")
