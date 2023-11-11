from models import model


def create_new_user():
    
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
    read = model.created_user.read_all()

    if read != "Error in select all users!":

        for client, account in read:
            print("-" * 20)
            print(f" Name: {client.name} \n CPF: {client.cpf} \n Address: {client.address} \n Account: {account.type_account} \n Agency: {account.agency} \n Number accont: {account.num_accont}")
            print("-" * 20)
    else:
        print("Error client not exist or deleted")


def read_user(cpf):

    user, account = model.created_user.read_user(cpf)

    return f" Id: {user.id} \n Name: {user.name} \n CPF: {user.cpf} \n Address: {user.address} \n Account: {account.type_account} \n Agency: {account.agency}"
    


def delete_user():

    cpf_user = int(input("Insert CPF: \n"))
    delete = model.created_user.delete_user(cpf_user)

    return delete


def update_client():
    
    cpf_edit = int(input("Insert CPF for search: \n"))

    if cpf_edit:

        print("_"*10,"REGISTERED DATA","_"*10)
        print(read_user(cpf_edit))
        print("_"*30)

        address = input("Insert address: \n")
        type_account = input("Input type account \n By default the account type is basic, if this is the case you don't need to enter: \n")

        if type_account == '':
            type_account = None

        model.created_user.edit_user(cpf_edit, address, type_account)
        return "Update sucessfully"
    else:
        return f"User not found check the CPF entered: {cpf_edit}"