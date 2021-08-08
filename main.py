import json
from db_manager import manage_password, save_password
from utils import random_password_generator, hash_password, check_password


def generate_password():
    service_name = input("Enter Name of Service,\n")
    username = input("Enter username for the Service,\n")

    password_length = int(input("Enter Length of Password,\n"))

    while True:
        include_special_chars_response = input("To add special characters in your password Choose,\
        \ny/Y for Yes\nn/N for No\n")
        if include_special_chars_response == "y" or include_special_chars_response == "Y":
            password = random_password_generator(password_length, include_special_chars=True)
            break
        elif include_special_chars_response == "n" or include_special_chars_response == "N":
            password = random_password_generator(password_length, include_special_chars=False)
            break
        else:
            password = ""
            print("please enter y/Y for Yes or n/N for Yes")
            continue

    print(f"\nYour Password For {service_name} : " + password + "\n")

    while True:
        save_pass_response = input(f"To save your password  for {service_name} Choose,\ny/Y for Yes\
        \nn/N for No\n")
        if save_pass_response == "y" or save_pass_response == "Y":
            save_password(service_name=service_name, username=username, password=password)
            break
        elif save_pass_response == "n" or save_pass_response == "N":
            break
        else:
            print("Please answer,\ny/Y for Yes\nn/N for No.")
            continue


def set_master_pass():
    master_pass_input1 = input("Plese Set Master Password for this service,\nEnter Master Password,\n")
    master_pass_input2 = input("Enter Again Master Password,\n")
    if master_pass_input1 == master_pass_input2:
        master_pass = hash_password(master_pass_input2)
        initial_dict = {
            "master_password": master_pass,
            "password_list": []
        }
        with open("pass_db.json", "w") as wfile:
            wfile.write(json.dumps(initial_dict))

    print("Your Master Password is Saved Successfully.\n")


def main_function():
    got_access = False
    try:
        with open("pass_db.json", "r") as rfile:
            pass_dict = json.loads(rfile.read())
    except json.decoder.JSONDecodeError:
        initial_dict = {
            "master_password": "",
            "password_list": []
        }
        with open("pass_db.json", "w") as wfile:
            wfile.write(json.dumps(initial_dict))

        with open("pass_db.json", "r") as rfile:
            pass_dict = json.loads(rfile.read())

    if pass_dict["master_password"] == "":
        set_master_pass()
        got_access = True
    else:
        max_attempts = 5
        attempt_count = 0
        while (not got_access) and (attempt_count < max_attempts):
            attempt_count += 1
            master_password = input("Enter the Master Password,\n")
            if check_password(hashed_password=pass_dict["master_password"], user_password=master_password):
                print("Welcome Master !!!\n")
                got_access = True
            else:
                print("You Entered Wrong Master Password, Try Again !!!\n")

    if got_access:
        while True:
            choice_dict = {
                "1": "Generate New Random Password",
                "2": "Save Your Password",
                "3": "Manage Your Passwords",
                "4": "Exit"
            }

            choice_str = "Enter The Number of Wanted Action,"
            for key, value in choice_dict.items():
                choice_str += f"\n{key}. {value}"
            choice_str += "\n"

            choice_made = int(input(choice_str))

            if choice_made in range(0, len(choice_dict)+1):
                print("You Are Going to " + choice_dict[str(choice_made)])
                if choice_made == 1:
                    generate_password()
                elif choice_made == 2:
                    save_password()
                elif choice_made == 3:
                    manage_password()
                elif choice_made == 4:
                    print("Good Bye !!!")
                    break
            else:
                continue


if __name__ == '__main__':
    main_function()
