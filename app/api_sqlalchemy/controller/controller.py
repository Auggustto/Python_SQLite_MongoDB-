from models import model


def create_new_user():
    """
    This function prompts the user to input information for creating a new user.
    It then creates a new user and inserts it into the database.

    User Input:
    - name (str): Full name of the user.
    - cpf (int): CPF (Brazilian ID) of the user.
    - address (str): Address of the user.
    - type_account (str): Type of account (default: 'basic').
    - agency (str): Agency where the account is held (selected from available options).
    - num_accont (int): Account number.

    Returns:
    - str: Success message or error if user creation fails.
    """
    
    name = str(input("Input full name: \n"))
    cpf = int(input("Input CPF: \n"))
    address = str(input("Input address: \n"))
    type_account = str(input("Input type account \n By default the account type is basic, if this is the case you don't need to enter: \n"))
    agency = str(input("Input agency: \n 1 Santander \n 2 Bradesco \n 3 Banco do Brasil \n 4 Caixa \n"))
    num_accont = int(input("Input number acccount: \n"))

    select_agency = {
        "1": "Santander",
        "2": "Bradesco",
        "3": "Banco do Brasil",
        "4": "Caixa",
    }

    if type_account == '':
        type_account = None

    create_user = model.created_user(name=name, cpf=cpf, address=address, type_account=type_account, agency=select_agency[agency], num_accont=num_accont)
    result = create_user.create()
    print(result)


def read_all_users():
    """
    This function retrieves information for all users and their associated accounts from the database.

    Returns:
    - None: Prints user and account information for all users.
    """
    read = model.created_user.read_all()

    if read != "Error in select all users!":

        for client, account in read:
            print(f" Name: {client.name} \n CPF: {client.cpf} \n Address: {client.address} \n Account: {account.type_account} \n Agency: {account.agency} \n Number accont: {account.num_accont}")
    else:
        print("Error client not exist or deleted")


def read_user(cpf):
    """
    This function retrieves information for a specific user and their associated accounts based on CPF.

    Parameters:
    - cpf (int): CPF of the user to retrieve.

    Returns:
    - str: User and account information or an error message if the user is not found.
    """

    try:
        user = model.created_user.read_user(cpf)
        
        if user:
                user_info = {
                    "id": user.id,
                    "name": user.name,
                    "cpf": user.cpf,
                    "address": user.address,
                }

                accounts_info = []

                for account in user.accounts:
                    account_info = {
                        "id": account.id,
                        "type_account": account.type_account,
                        "agency": account.agency,
                        "num_accont": account.num_accont,
                    }
                    accounts_info.append(account_info)

                user_info["accounts"] = accounts_info

                return f" ID: {user_info['id']} \n Name: {user_info['name']} \n CPF: {user_info['cpf']} \n Address: {user_info['address']} \n Type accounts: {user_info['accounts'][0]['type_account']} \n Agency: {user_info['accounts'][0]['agency']} \n Number account: {user_info['accounts'][0]['num_accont']}"
                

        else:
            return f"User not found with CPF: {cpf}"

    except Exception as e:
        return f"Error in reading user and accounts: {e}"
    


def delete_user():
    """
    This function prompts the user to input a CPF and deletes the corresponding user and their accounts from the database.

    Returns:
    - str: Success message or error if deletion fails.
    """

    cpf_user = int(input("Insert CPF: \n"))
    delete = model.created_user.delete_user(cpf_user)

    print(delete)


def update_client():
    """
    This function prompts the user to input a CPF, displays the existing user information,
    and allows the user to update the address and type of account for the user.

    Returns:
    - str: Success message or error if update fails.
    """
    
    cpf_edit = int(input("Insert CPF for search: \n"))

    if cpf_edit:

        print("_"*10,"REGISTERED DATA","_"*10)
        print(read_user(cpf_edit))
        print("_"*30)

        address = input("Insert address: \n")
        type_account = input("Input type account \n")

        if type_account == '':
            type_account = None

        update = model.created_user.edit_user(cpf_edit, address, type_account)
        return update
    else:
        return f"User not found check the CPF entered: {cpf_edit}"