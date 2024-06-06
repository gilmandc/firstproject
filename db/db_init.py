import sqlite3

connection = sqlite3.connect("/home/daniel/pythonprojects/firstproject/recipe_book.db")
cursor = connection.cursor()

def create_table():    
    table_init_script = "CREATE TABLE IF NOT EXISTS recipes (name TEXT PRIMARY KEY, meal_type TEXT, protein TEXT, cuisine TEXT, time_req INTEGER)" 
    cursor.execute(table_init_script)
    connection.commit()

