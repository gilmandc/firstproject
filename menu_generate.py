import json
import random
from entree_class import Entree

def menu_gen():
    days_in_menu = int(input('Create menu for how many days?\n'))
    
    # load book.json as a dictionary
    with open('book.json', 'r') as x:
        for line in x:
            choice_dict = json.load(line)    
            
        return choice_dict
    
    # have it returned and be cast into the entree class
    
    # list of entrees already generated
    used_breakfasts = []
    used_lunches = []
    used_dinners = []
    
    for i in range(days_in_menu):
        choices.pop[used_breakfasts, used_lunches, used_dinners]
        random_breakfast = random.choice(Entree.name[breakfast])
        random_lunch = random.choice(Entree.name[lunch])
        random_dinner = random.choice(Entree.name[dinner])
        used_breakfasts.append(random_breakfast)
        used_lunches.append(random_lunch)
        used_dinners.append(random_dinner)
        
        print f'Day {i+1} | Breakfast:{random_breakfast}\n'
        print f'Day {i+1} | Lunch: {random_lunch}\n'
        print f'Day {i+1} | Dinner:{random_dinner}\n'
               

menu_gen()
    
    

        