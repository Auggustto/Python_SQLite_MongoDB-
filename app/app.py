from controller import controller


select_options = input(" \n Select the desired option: \n 1 -> Create user \n 2 -> De1lete user \n 3 -> Edit user \n 4 -> View all users \n 5 -> Read user \n 6 -> Exit \n ")

select_function = {
    "1":controller.create_new_user,
    "2":controller.delete_user,
    "3":controller.update_client,
    "4":controller.read_all_users,
    "5": controller.read_user,
}


if select_options <= "5":
    print("_" * 40)
    select_f = select_function[select_options]()
    print("_" * 40)
else:
    print("Operation finished")