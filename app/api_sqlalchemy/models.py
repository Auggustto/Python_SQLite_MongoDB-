from db_sqlalchemy import Client
from db_sqlalchemy import Account
from db_sqlalchemy import session

class created_user:
    def __init__(self, name, cpf, address, type_account, agency):
        self.name = name
        self.cpf = cpf
        self.address = address
        self.type_account = type_account
        self.agency = agency

    def create(self):

        new_client = Client(name=self.name, cpf=self.cpf, address=self.address)
        new_account = Account(type_account=self.type_account, agency=self.agency)

        try:
            session.add(new_client)
            session.add(new_account)
            session.commit()

            return "User created sucessfully"
        
        except TypeError as e:
            return f"Error in create user {e}"
    
    def read_all():
        results = session.query(Client, Account).join(Account).all()
        
        try:
            return results
        except TypeError as e:
            return f"Error in select all users! '\n' Error: {e}"
    




# teste = created_user("leonardo", 123, "R: av 1234")
# test = teste.create()

teste2 = Account()
print(teste2.type_account)




