from entree_class import Entree


# accepting user input
def get_input():
    name = input("What is the name of the entree? \n")
    meal_type = input("Which meal of the day is it served? \n")
    protein = input("What is the main protein in the entree? \n")
    cuisine = input("What type of cuisine is this? \n")
    time_req = input("From 1, 2, or 3, what is the time requirement?\n(1: Quick, 2: Normal Prep, 3: Advance Prep): \n")

    
    new_entree = Entree(name, meal_type, protein, cuisine, time_req)            # creating a new class instance
    
                                                                                  
                                                                                # take new_entree and insert into dictionary
    
   
get_input()     
  

