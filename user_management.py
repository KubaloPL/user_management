import json
import random
import re
import os

DATA_PATH = "data/"
USER_DATABASE_PATH = f"{DATA_PATH}users.json"

users = []

def add_user(user_data: dict): 
    '''
    Adds a new user.
    DATA TEMPLATE:  -- User id is generated incrementally
     1 = {
     "name": "Jakub",
     "nip": 12345,
     "pesel": "59124",
     "regon": 122345,
     "password": "123"
    }
    '''
    load_users_from_file(users)

    if validate_pesel(user_data["pesel"]):
        print("BŁĄD: Nieprawidłowy PESEL")
        return
    if validate_nip(user_data["nip"]):
        print("BŁĄD: Nieprawidłowy NIP")
        return
    if validate_nip(user_data["regon"]):
        print("BŁĄD: Nieprawidłowy REGON")
        return
    if validate_nip(user_data["password"]):
        print("BŁĄD: Hasło jest zbyt słabe")
        return

    users.append(user_data)

    save_users_to_file(users)

def save_users_to_file(users):
    file = open(USER_DATABASE_PATH,"w")
    json.dump(users, file)
    file.close()

def load_users_from_file():
    global users
    file = open(USER_DATABASE_PATH, "r")
    users = json.load(file)

def remove_user(user_id): 
    '''
    Usuwa istniejącego użytkownika.
    '''


    
def edit_user(user_id:int, updated_data:dict): 
    '''
    Edytuje dane użytkownika.
    '''
    load_users_from_file()
    for key, value in updated_data.items():
        users[user_id][key] = value
    save_users_to_file(users)


def validate_nip(nip): 
    '''
    Waliduje numer NIP.
    '''
    pass



def validate_pesel(pesel): 
    '''
    Waliduje numer PESEL.
    '''
    pass



def validate_regon(regon): 
    '''
    Waliduje numer REGON.
    '''
    pass



def generate_password(): 
    '''
    Generuje silne hasło.
    '''
    pass


    
def validate_password(password): 
    '''
    Waliduje siłę hasła.
    '''
    pass

load_users_from_file()
print(users)

edit_user(0,{"name": "Hello"})