from entree_class import Entree
from enums import RedMeat
from enums import Protein


# accepting user input



def get_input():
    user_stop = ""
    book = []

    while user_stop != "No" or "no" or "NO" or "nO": 
        name = input("What is the name of the entree? \n")
        meal_type = input("Which meal of the day is it served? \n")
        protein = input("What is the main protein in the entree? \n")
        cuisine = input("What type of cuisine is this? \n")
        time_req = input("From 1, 2, or 3, what is the time requirement?\n(1: Quick, 2: Normal Prep, 3: Advance Prep): \n")
        user_stop = input("Do you want to add another item?\n (Enter 'No' if finished)\n")
        new_entree = Entree(name, meal_type, protein, cuisine, time_req)
        book.append(new_entree)
    for entree in book:
        print('Items in your menu book:\n')
        print(entree.name)

    
        
                                                                                     
get_input()     
  

