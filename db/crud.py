import sqlite3
from enums import Meal

connection = sqlite3.connect("/home/daniel/pythonprojects/firstproject/recipe_book.db")
cursor = connection.cursor()


def insert_entry(meal_to_insert:Meal):
    query_string = f"""INSERT INTO recipes (name, meal_type, protein, cuisine, time_req) 
    VALUES ("{meal_to_insert.name}", "{meal_to_insert.meal_type}", "{meal_to_insert.protein}", "{meal_to_insert.cuisine}", "{meal_to_insert.time_req}")"""
    cursor.execute(query_string)
    connection.commit() 

def delete_entry(user_input: str):
    query_string = f"DELETE FROM recipes WHERE name = '{user_input}'"
    cursor.execute(query_string)
    connection.commit()

def fetch_all():
    query_string = "SELECT * FROM recipes"
    results = cursor.execute(query_string)
    connection.commit()
    return results.fetchall()