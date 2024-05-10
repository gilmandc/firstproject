from entree_class import Entree
import json
from db.crud import insert_meal, fetch_all


# accepting user input
# def default_json(t): 
#     return f'{t}'

def get_input():
    user_stop = ""
        

    while user_stop != "no":
        entree_exists = False
        name = input("What is the name of the entree? \n")
        
                
        if entree_exists is False:
            meal_type = input("Which meal of the day is it served? \n")
            protein = input("What is the main protein in the entree? \n")
            cuisine = input("What type of cuisine is this? \n")
            time_req = input("From 1, 2, or 3, what is the time requirement?\n(1: Quick, 2: Normal Prep, 3: Advance Prep): \n")
            user_stop = input("Do you want to add another item?\n (Enter 'No' if finished)\n")
            
            insert_meal(meal_name=name, meal_type=meal_type, protein=protein, cuisine=cuisine, time_req=time_req)
            print(fetch_all())
            
        
get_input()     