from models import models


def formatting_returns(user):
    """
    Formats the data from a user dictionary for proper display and returns a formatted string.
    
    Args:
        user (dict): Dictionary containing user information.
    
    Returns:
        str: Formatted string with user information.
    """
    return f"\n ID: {user['_id']} \n Name: {user['name']} \n CPF: {user['cpf']} \n Address: {user['address']} \n Account: {user['account']['type']} \n Agency: {user['account']['agency']} \n Number account: {user['account']['number']} \n Date register: {user['date_time']}"



def create_new_user():
    """
    Collects user input to create a new user and prints the result.
    """

    name = str(input("Input full name: \n"))
    cpf = int(input("Input CPF: \n"))
    address = str(input("Input address: \n"))
    type_account = str(input("Input type account \n By default the account type is basic, if this is the case you don't need to enter: \n"))
    agency = str(input("Input agency: \n 1 Santander \n 2 Bradesco \n 3 Banco do Brasil \n 4 Caixa \n"))
    num_account = int(input("Input number acccount: \n"))

    if type_account == "":
        type_account = "Basic"

    select_agency = {
        "1": "Santander",
        "2": "Bradesco",
        "3": "Banco do Brasil",
        "4": "Caixa",
    }

    create = models.create_user(name=name, cpf=cpf, address=address,type_account=type_account, agency=select_agency[agency], num_account=num_account)
    result = create.create()

    print(result)



def read_user():
    """
    Collects user input for CPF, reads user information, formats it, and prints the details.
    """

    cpf_search = int(input("Insert CPF: \n"))

    user = models.create_user.read_user(cpf_search)
    print(user)

    if user != "Invalid CPF error or user has been deleted":
        metadata = formatting_returns(user)

        print("_"*20, "Account details","_"*20)
        # print(f"\n ID: {user['_id']} \n Name: {user['name']} \n CPF: {user['cpf']} \n Address: {user['address']} \n Account: {user['account']['type']} \n Agency: {user['account']['agency']} \n Number account: {user['account']['number']} \n Date register: {user['date_time']}")
        print(metadata)
        print("_"*40)
    else:
        print(user)



def delete_user():
    """
    Collects user input for CPF, deletes the user, and prints the result.
    """
    cpf_delete = int(input("Insert CPF: \n"))

    result = models.create_user.delete_user(cpf_delete)

    print(result)



def update_client():
    """
    Collects user input for CPF, reads user information, formats it, prints the details,
    updates the client, and prints the update result.
    """

    cpf_edit = int(input("Insert CPF for search: \n"))

    user = models.create_user.read_user(cpf_edit)

    if user != "Invalid CPF error or user has been deleted":
        metadata = formatting_returns(user)

        print("_"*20, "Account details","_"*20)
        print(metadata)
        print("_"*40)
        
        update = models.create_user.update_client(user['cpf'])
        print(update)

    else:
        print(user)


def read_all_users():
    """
    Reads all users, formats the information for each user, and prints the details.
    """

    all_users = models.create_user.read_all_users()

    for user in all_users:

        result = formatting_returns(user)

        print("_"*20, "Account details","_"*20)
        print(result)
        print("_"*40)


