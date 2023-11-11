from db import db_sqlalchemy


class created_user:
    """
        Initialize the created_user object with user data.

        Parameters:
        - name (str): User's name.
        - cpf (int): User's CPF (Brazilian ID).
        - address (str): User's address.
        - type_account (str): Type of account (default: 'basic').
        - agency (str): Account agency information.
        - num_accont (int): Account number.

        Attributes:
        - name (str): User's name.
        - cpf (int): User's CPF (Brazilian ID).
        - address (str): User's address.
        - type_account (str): Type of account (default: 'basic').
        - agency (str): Account agency information.
        - num_accont (int): Account number.
    """
    def __init__(self, name, cpf, address, type_account, agency, num_accont):
        self.name = name
        self.cpf = cpf
        self.address = address
        self.type_account = type_account
        self.agency = agency
        self.num_accont = num_accont

    def create(self):
        """
            Insert a new user into the database.

            Returns:
            - str: Success message or error if the creation fails.
        """

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
        """
        Retrieve all users and their associated accounts from the database.

        Returns:
        - list: List of tuples containing user and account information.
                Each tuple consists of a Client object and an Account object.
        - str: Error message if the retrieval fails.
        """
        statements = db_sqlalchemy.session.query(db_sqlalchemy.Client,db_sqlalchemy.Account).join(db_sqlalchemy.Client).all()
        
        if statements:
            return statements
        else:
            return f"Error in select all users!"
    
    def read_user(cpf_user):
        """
        Retrieve a user and their associated accounts based on CPF.

        Parameters:
        - cpf_user (int): User's CPF to search for.

        Returns:
        - Client: Client object containing user information.
        - str: Error message if the retrieval fails.
        """
        
        statements = db_sqlalchemy.session.query(db_sqlalchemy.Client).filter_by(cpf=cpf_user).first()
        
        return statements
    

    def delete_user(cpf_delete):
        """
        Delete a user and their associated accounts from the database.

        Parameters:
        - cpf_delete (int): User's CPF to delete.

        Returns:
        - str: Success message or error if the deletion fails.
        """
        delete = db_sqlalchemy.session.query(db_sqlalchemy.Client).filter_by(cpf=cpf_delete).first()
        db_sqlalchemy.session.delete(delete)
        db_sqlalchemy.session.commit()

        return "User deleted sucessfully"
    

    def edit_user(cpf_edit, address, type_account):
        """
        Edit a user's address and associated account types in the database.

        Parameters:
        - cpf_edit (int): User's CPF to edit.
        - address (str): New address for the user.
        - type_account (str): New type for associated accounts.

        Returns:
        - str: Success message or error if the update fails.
        """

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






