from db_sqlalchemy import Client
from db_sqlalchemy import Account
from db_sqlalchemy import session
from db_sqlalchemy import select

class created_user:
    def __init__(self, name, cpf, address, type_account, agency):
        self.name = name
        self.cpf = cpf
        self.address = address
        self.type_account = type_account
        self.agency = agency

    def create(self):
        # print(self.name, self.cpf, self.address, self.type_account, self.agency)

        new_client = Client(name=self.name, cpf=self.cpf, address=self.address)
        new_account = Account(type_account=self.type_account, agency=self.agency)

        ### Relation of client and account
        new_client.account = new_account

        try:
            session.add(new_client)
            session.commit()

            # session.add(new_account)
            # session.commit()

            return "User created sucessfully"
        
        except Exception as e:
            session.rollback()
            return f"Error in creating user: {e}"
    
    @staticmethod
    def read_all():
        statements = session.query(Client,Account).join(Client).all()
        
        if statements:
            return statements
        else:
            return f"Error in select all users!"
    
    def read_user(cpf_user):
        # statements = session.query(Client).filter_by(cpf=cpf_user).first()
        statements = session.query(Client, Account).join(Account).filter(Client.cpf == cpf_user).first()
        
        return statements




