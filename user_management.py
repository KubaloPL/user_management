import json
import random
import re
import os
import string

DATA_PATH = "data/"
USER_DATABASE_PATH = f"{DATA_PATH}users.json"

users = []

pasword_character_list = ""
pasword_character_list += string.ascii_letters
pasword_character_list += string.digits
pasword_character_list += string.punctuation

def add_user(user_data: dict): 
    '''
    Adds a new user.
    DATA TEMPLATE:  -- User id is generated incrementally
     1 = {
     "name": "Jakub",
     "nip": 12345,
     "pesel": "59124",
     "regon": 122345,
     "password": "123",
     "status": "Registered" -- Registered | Removed
    }
    '''
    load_users_from_file(users)

    if validate_pesel(user_data["pesel"]) == False:
        print("BŁĄD: Nieprawidłowy PESEL")
        return False
    if validate_nip(user_data["nip"]) == False:
        print("BŁĄD: Nieprawidłowy NIP")
        return False
    if validate_nip(user_data["regon"]) == False:
        print("BŁĄD: Nieprawidłowy REGON")
        return False
    if validate_nip(user_data["password"]) == False:
        print("BŁĄD: Hasło jest zbyt słabe")
        return False

    users.append(user_data)

    save_users_to_file(users)

def save_users_to_file(users):
    if not os.path.exists(USER_DATABASE_PATH):
        open(USER_DATABASE_PATH,"x")

    file = open(USER_DATABASE_PATH,"w")
    json.dump(users, file)
    file.close()

def load_users_from_file():
    if not os.path.exists(USER_DATABASE_PATH):
        open(USER_DATABASE_PATH,"x")

    global users
    file = open(USER_DATABASE_PATH, "r")
    users = json.load(file)

def remove_user(user_id): 
    '''
    Usuwa istniejącego użytkownika.
    '''
    load_users_from_file()
    users[user_id]["pesel"] = ""
    users[user_id]["password"] = ""
    users[user_id]["status"] = "Removed"
    save_users_to_file(users)

    
def edit_user(user_id:int, updated_data:dict): 
    '''
    Edytuje dane użytkownika.
    '''
    load_users_from_file()
    for key, value in updated_data.items():
        users[user_id][key] = value
    save_users_to_file(users)


def validate_nip(nip:str): 
    '''
    Waliduje numer NIP.
    '''
    nip = nip.replace('-', '')
    if len(nip) != 10 or not nip.isdigit(): 
        print("BŁĄD: NIP powinien być 10 cyfrowym numerem")
        return False

    digits = [int(i) for i in nip]
    weights = (6, 5, 7, 2, 3, 4, 5, 6, 7)

    check_sum = sum(d * w for d, w in zip(digits, weights)) % 11
    if check_sum == digits[9]:
        return True
    else:
        print("BŁĄD: Suma kontrolna numeru NIP nie zgadza się")
        return False



def validate_pesel(pesel): 
    '''
    Waliduje numer PESEL.
    '''
    if len(pesel) != 11 or not pesel.isdigit(): 
        print("BŁĄD: PESEL powinien być 11 cyfrowym numerem")
        return False

    digits = [int(i) for i in pesel]
    weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)

    check_sum = sum((d * w) % 10 for d, w in zip(digits, weights))
    check_sum = 10 - (check_sum % 10)
    if check_sum == digits[10]:
        return True
    else:
        print("BŁĄD: Suma kontrolna numeru PESEL nie zgadza się")
        return False



def validate_regon(regon): 
    '''
    Waliduje numer REGON.
    '''
    if not(len(regon) == 9 or len(regon) == 14) or not regon.isdigit(): 
        print("BŁĄD: REGON powinien być 9 lub 14 cyfrowym numerem")
        return False
    
    digits = [int(i) for i in regon]
    if len(regon) == 9:
        weights = (8, 9, 2, 3, 4, 5, 6, 7)
        check_sum = sum(d * w for d, w in zip(digits, weights)) % 11
        if check_sum == digits[8]:
            return True
        else:
            print("BŁĄD: Suma kontrolna numeru REGON nie zgadza się")
            return False
    else:
        weights = (2, 4, 8, 5, 0 , 9, 7, 3, 6, 1, 2, 4, 8)
        check_sum = sum(d * w for d, w in zip(digits, weights)) % 11
        if check_sum == digits[13]:
            return True
        else:
            print("BŁĄD: Suma kontrolna numeru REGON nie zgadza się")
            return False



def generate_password(): 
    '''
    Generuje silne hasło.
    '''
    while True:
        password = ""
        for i in range(12):
            randomchar = random.choice(pasword_character_list)
            password += randomchar
        if validate_password(password,dontprint=True) == True:
            break
    
    return password


    
def validate_password(password,dontprint = None):
    '''
    Waliduje siłę hasła.
    '''
    if len(password) < 12:
        if dontprint == None:
            print('BŁĄD: Długość hasła powinna wynosić co najmniej 12 znaków')
        return False
    
    if not any(char.isdigit() for char in password):
        if dontprint == None:
            print('BŁĄD: Hasło powinno zawierać co najmniej 1 cyfrę')
        return False
    
    if not any(char.isupper() for char in password):
        if dontprint == None:
            print('BŁĄD: Hasło powinno zawierać co najmniej 1 dużą literę')
        return False

    if not any(char.islower() for char in password):
        if dontprint == None:
            print('BŁĄD: Hasło powinno zawierać co najmniej 1 małą literę')
        return False

    if not any(char in string.punctuation for char in password):
        if dontprint == True:
            print('BŁĄD: Hasło powinno zawierać co najmniej 1 specjalny znak')
        return False
    
    return True


# Example usage:

# # Adding a new user
# new_user = {
#     "name": "Jan Kowalski",
#     "nip": "1234567890",
#     "pesel": "44051401458",
#     "regon": "123456789",
#     "password": generate_password(),
#     "status": "Registered"
# }
# add_user(new_user)

# # Removing a user
# remove_user(0)

# # Editing a user
# edit_user(1, {"name": "New Name"})