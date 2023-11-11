from db import db_sqlalchemy


class created_user:
    def __init__(self, name, cpf, address, type_account, agency, num_accont):
        self.name = name
        self.cpf = cpf
        self.address = address
        self.type_account = type_account
        self.agency = agency
        self.num_accont = num_accont

    def create(self):
        # print(self.name, self.cpf, self.address, self.type_account, self.agency)

        new_client = db_sqlalchemy.Client(name=self.name, cpf=self.cpf, address=self.address)
        new_account = db_sqlalchemy.Account(type_account=self.type_account, agency=self.agency, num_accont = self.num_accont)

        ### Relation of client and account ###
        new_client.accounts.append(new_account)

        try:
            db_sqlalchemy.session.add(new_client)
            db_sqlalchemy.session.commit()
            
            return "User created sucessfully"
        
        except Exception as e:
            db_sqlalchemy.session.rollback()
            return f"Error in creating user: {e}"
    
    @staticmethod
    def read_all():
        statements = db_sqlalchemy.session.query(db_sqlalchemy.Client,db_sqlalchemy.Account).join(db_sqlalchemy.Client).all()
        
        if statements:
            return statements
        else:
            return f"Error in select all users!"
    
    def read_user(cpf_user):
        # statements = session.query(Client).filter_by(cpf=cpf_user).first()
        # statements = db_sqlalchemy.session.query(db_sqlalchemy.Client).join(db_sqlalchemy.Client.accounts).filter(db_sqlalchemy.Client.cpf == cpf_user).first()
        statements = db_sqlalchemy.session.query(db_sqlalchemy.Client).filter_by(cpf=cpf_user).first()
        
        return statements
    

    def delete_user(cpf_delete):
        delete = db_sqlalchemy.session.query(db_sqlalchemy.Client).filter_by(cpf=cpf_delete).first()
        db_sqlalchemy.session.delete(delete)
        db_sqlalchemy.session.commit()

        return "User deleted sucessfully"
    

    def edit_user(cpf_edit, address, type_account):

        try:
            edit = db_sqlalchemy.session.query(db_sqlalchemy.Client).filter_by(cpf=cpf_edit).first()
            print("Edit", edit.address)

            if edit:
                edit.address = address

                for account in edit.accounts:
                    account.type_account = type_account

                    db_sqlalchemy.session.commit()

                    return "Client updated successfully"

                else:
                    return f"Account with type_account {type_account} not found for the client"
            else:
                return f"Client not found with CPF: {cpf_edit}"
            
        except Exception as e:
            db_sqlalchemy.session.rollback()
            return f"Error in updating client: {e}"






