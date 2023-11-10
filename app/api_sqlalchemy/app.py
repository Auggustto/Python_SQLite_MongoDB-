from models import created_user


def create_new_user():
    
    name = str(input("Input full name:""\n"))
    cpf = int(input("Input CPF:""\n"))
    address = str(input("Input address:""\n"))
    type_account = str(input("Input type account '\n' By default the account type is basic, if this is the case you don't need to enter""\n"))
    agency = int(input("Input agency:""\n"))

    if type_account == '':
        type_account = None

    create_user = created_user(name=name, cpf=cpf, address=address, type_account=type_account, agency=agency)
    result = create_user.create()
    print(result)


def read_all_users():
    read = created_user.read_all()

    if read != "Error in select all users!":

        for client, account in read:
            print("-" * 20)
            print(f" Name: {client.name} \n CPF: {client.cpf} \n Address: {client.address} \n Account: {account.type_account} \n Agency: {account.agency}")
            print("-" * 20)
    else:
        print("Error in read client")


def read_user(cpf):

    user, account = created_user.read_user(cpf)

    print("-" * 20)
    print(f" Id: {user.id} \n Name: {user.name} \n CPF: {user.cpf} \n Address: {user.address} \n Account: {account.type_account} \n Agency: {account.agency}")
    print("-" * 20)


# def update_user(cpf):



# create_new_user()
read_all_users()
# read_user(12345678)