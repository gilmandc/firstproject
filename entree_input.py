from entree_class import Entree
import json


# accepting user input
# def default_json(t): 
#     return f'{t}'

def get_input():
    user_stop = ""
        

    while user_stop != "no":
        entree_exists = False
        name = input("What is the name of the entree? \n")
        
  

        # Checks if entree has already been input in book.json
        with open('book.json', 'r') as x:
            for line in x:
                try:
                    line_dict = json.loads(line)
                    if name.lower().replace('-',' ') == line_dict['name'].lower().replace('-',' '):
                        entree_exists = True
                        print('That entree already exists.')
                        break         
                except Exception:
                    pass
                
        if entree_exists is False:
            meal_type = input("Which meal of the day is it served? \n")
            protein = input("What is the main protein in the entree? \n")
            cuisine = input("What type of cuisine is this? \n")
            time_req = input("From 1, 2, or 3, what is the time requirement?\n(1: Quick, 2: Normal Prep, 3: Advance Prep): \n")
            user_stop = input("Do you want to add another item?\n (Enter 'No' if finished)\n")
            new_entree = Entree(name, meal_type, protein, cuisine, time_req)
            converted_entree = new_entree.to_dict()
            
            with open('book.json', 'a') as x:
                json.dump(converted_entree, x)
                x.write('\n')
    
        
get_input()     