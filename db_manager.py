import json
import string
from utils import random_password_generator


def save_password(service_name=None, username=None, password=None):
    with open("pass_db.json", "r") as rfile:
        pass_dict = dict(json.loads(rfile.read()))

    if len(pass_dict["password_list"]) > 0:
        last_key = int(pass_dict["password_list"][-1]["id"])
        next_key = last_key + 1
    else:
        next_key = 1

    if service_name is None and username is None and password is None:
        service_name = input("Enter Name of Service,\n")
        username = input("Enter username for the Service,\n")
        password = input("Enter your password for the Service,\n")

    new_item = {
        "id": next_key,
        "service_name": service_name,
        "username": username,
        "password": password
    }
    pass_dict["password_list"].append(new_item)

    with open("pass_db.json", "w") as wfile:
        wfile.write(json.dumps(pass_dict))

    print(f"Your Password for {service_name} is Saved Successfully.\n")


def modify_password():
    with open("pass_db.json", "r") as rfile:
        pass_dict = dict(json.loads(rfile.read()))

    id_num = int(input("Please Enter id number of password you want to modify,\n"))

    for item in pass_dict["password_list"]:
        if int(item["id"]) == int(id_num):
            service_name = item["service_name"]
            prev_pass_len = len(item["password"])

            for s in item["password"]:
                if s in string.punctuation:
                    prev_pass_include_special_char = True
                    break
                else:
                    prev_pass_include_special_char = False

            choice_num = int(input(
                f"Please Enter Your Choice for changing Password,\n1. Change YourSelf\n2. Generate Random Password\n"))
            if choice_num == 1:
                new_pass = input(f"Please Enter Your New Password for {service_name},\n")
            elif choice_num == 2:
                new_pass = random_password_generator(password_length=prev_pass_len,
                                                     include_special_chars=prev_pass_include_special_char)
            item["password"] = new_pass

            with open("pass_db.json", "w") as wfile:
                wfile.write(json.dumps(pass_dict))

            print(f"Your Password Modified Successfully for {service_name}.\n")
            break


def remove_password():
    with open("pass_db.json", "r") as rfile:
        pass_dict = dict(json.loads(rfile.read()))

    id_num = int(input("Please Enter id number of password you want to remove,\n"))

    index_num = -1
    for item in pass_dict["password_list"]:
        index_num += 1
        if int(item["id"]) == int(id_num):
            service_name = item["service_name"]
            choice_num = input(
                f"Are You Sure You Want to Remove Password for {service_name},\nEnter y/Y for Yes\nEnter n/N for No\n")
            if choice_num == "y" or choice_num == "Y":
                pass_dict["password_list"].pop(index_num)

                for i in list(pass_dict["password_list"])[index_num:]:
                    i["id"] -= 1

            with open("pass_db.json", "w") as wfile:
                wfile.write(json.dumps(pass_dict))

            print(f"Your Password Removed Successfully for {service_name}.\n")
            break


def see_passwords():
    print()
    with open("pass_db.json", "r") as rfile:
        pass_dict = dict(json.loads(rfile.read()))

    for item in pass_dict["password_list"]:
        for k, v in dict(item).items():
            print(f"{k} : {v}")
        print()


def manage_password():
    while True:
        choice_num = int(input(
            f"Please Enter Your Choice for managing Password,\n1. Modify Password\n2. Remove Password\n3. See Passwords\n4. Exit\n"))

        if choice_num == 1:
            modify_password()
            see_passwords()
            break
        elif choice_num == 2:
            remove_password()
            see_passwords()
            break
        elif choice_num == 3:
            see_passwords()
            continue
        elif choice_num == 4:
            break
