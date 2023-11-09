from models import created_user


def create_user():
    
    name = str(input("Input full name:""\n"))
    cpf = int(input("Input CPF:""\n"))
    address = str(input("Input address:""\n"))
    type_account = str(input("Input type account '\n' By default the account type is basic, if this is the case you don't need to enter""\n"))
    agency = int(input("Input agency:""\n"))

    create_user = created_user(name=name, cpf=cpf, address=address, type_account=type_account, agency=agency)
    c_user = create_user.create()
    print(c_user)

def read_all_users():
    read = created_user.read_all()

    for client, account in read:
        print("name",client.name)
        print("account",account.type_account)


