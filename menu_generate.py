import sqlite3

connection = sqlite3.connect('/home/daniel/pythonprojects/firstproject/recipe_book.db')
cursor = connection.cursor()

days_in_menu = int(input('Create menu for how many days?\n'))
def menu_gen(days_in_menu: int):
    meals = cursor.execute(f"""
    SELECT name 
    FROM recipes
    ORDER BY random() 
    LIMIT {days_in_menu} ;
    """)
    print(meals)


menu_gen(days_in_menu)