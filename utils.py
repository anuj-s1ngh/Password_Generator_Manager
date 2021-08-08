import secrets
import string
import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    # print(salt)
    hashed_pass = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    # print(hashed_pass)
    return hashed_pass


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def random_password_generator(password_length=16, include_special_chars=True):
    num = password_length  # define the length of the string

    # define the secrets.choice() method and pass the string.ascii_letters + string.digits as an parameters.
    if include_special_chars:
        res = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(num))
    else:
        res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
    # Print the Secure string with the combination of letters, digits and punctuation
    # print("Secure random string is :" + str(res))
    return str(res)

