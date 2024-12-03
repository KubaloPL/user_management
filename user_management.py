import json
import random
import re
import os

users = []

def add_user(user_data: dict): 
    '''
    Dodaje nowego użytkownika.
     {
     "user_id": 1,
     "name": "Jakub",
     "nip": 12345,
     "pesel": "59124",
     "regon": 122345,
     "password": "123"
    }
    '''

    users.append(user_data)
    json.dump()

def save_users_to_file(users):
    pass

def remove_user(user_id): 
    '''
    Usuwa istniejącego użytkownika.
    '''


    
def edit_user(user_id, updated_data): 
    '''
    Edytuje dane użytkownika.
    '''



def validate_nip(nip): 
    '''
    Waliduje numer NIP.
    '''



def validate_pesel(pesel): 
    '''
    Waliduje numer PESEL.
    '''



def validate_regon(regon): 
    '''
    Waliduje numer REGON.
    '''



def generate_password(): 
    '''
    Generuje silne hasło.
    '''


    
def validate_password(password): 
    '''
    Waliduje siłę hasła.
    '''

