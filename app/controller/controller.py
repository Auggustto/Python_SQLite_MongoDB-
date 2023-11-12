from models import models

def create_new_user():

    name = str(input("Input full name: \n"))
    cpf = int(input("Input CPF: \n"))
    address = str(input("Input address: \n"))
    type_account = str(input("Input type account \n By default the account type is basic, if this is the case you don't need to enter: \n"))
    agency = str(input("Input agency: \n 1 Santander \n 2 Bradesco \n 3 Banco do Brasil \n 4 Caixa \n"))
    num_accont = int(input("Input number acccount: \n"))

    if type_account == "":
        type_account = "Basic"

    select_agency = {
        "1": "Santander",
        "2": "Bradesco",
        "3": "Banco do Brasil",
        "4": "Caixa",
    }

    create = models.create_user(name=name, cpf=cpf, address=address,type_account=type_account, agency=select_agency[agency], num_accont=num_accont)

    return create


