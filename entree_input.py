from pluralizer import Pluralizer
from db.crud import insert_entry, fetch_all, delete_entry
from db.db_init import create_table
from enums import Meal
from sqlite3 import IntegrityError
import sys


def get_input():
    user_stop = ''
    pluralize = Pluralizer()
    while user_stop != 'No' or 'NO' or 'N' or 'n':
        name = pluralize.singular(word=input("What is the name of the entree? \n").lower())
        meal_type = set(input("Which meals of the day is this served? (B,L,D) \n").lower())
        protein = input("What is the main protein in the entree? \n").lower()
        cuisine = input("What type of cuisine is this? \n").lower()    
        
        time_req = 0
        while time_req not in [1,2,3]:
            print('Please choose either 1, 2, or 3')
            time_req = int(input("From 1, 2, or 3, what is the time requirement?\n(1: Quick, 2: Normal Prep, 3: Advance Prep): \n"))
        
        this_meal = Meal(name=name, meal_type=meal_type, protein=protein, cuisine=cuisine, time_req=time_req)    
        try:
            insert_entry(this_meal)
        except Exception as e:
            if isinstance(e, IntegrityError):
                print('This entry already exists. Please delete or add a different one.')


            
        user_stop = input("Do you want to add another item?\n (Enter 'No' if finished)\n")
        return user_stop

    

create_table()

while True: 
    select_action = input('Would you like to read (R), add (A), or delete (D) entries? [E to exit] ').lower() 
    if select_action == 'r':
        print(fetch_all())
    if select_action == 'd':
        meal_to_delete = input('Name of meal to be deleted: [E to exit]')
        delete_entry(meal_to_delete)
    if select_action == 'a':
        get_input()
    if select_action == 'e':
        sys.exit()






     