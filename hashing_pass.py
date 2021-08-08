import uuid
import hashlib


def hash_password(password):
    # this fuction is taken from https://www.pythoncentral.io/hashing-strings-with-python/.
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    print(salt)
    hashed_pass = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    print(hashed_pass)
    return hashed_pass


def check_password(hashed_password, user_password):
    # this fuction is taken from https://www.pythoncentral.io/hashing-strings-with-python/.
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


if __name__ == '__main__':
    new_pass = input('Please enter a password: ')
    hashed_password = hash_password(new_pass)
    print('The string to store in the db is: ' + hashed_password)
    old_pass = input('Now please enter the password again to check: ')
    if check_password(hashed_password, old_pass):
        print('You entered the right password')
    else:
        print('I am sorry but the password does not match')

