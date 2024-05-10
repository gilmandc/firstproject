import sqlite3

connection = sqlite3.connect("/home/daniel/pythonprojects/firstproject/recipe_book.db")
cursor = connection.cursor()



def insert_meal(meal_name: str, meal_type: str, protein: str, cuisine: str, time_req: int):
    query_string = f'INSERT INTO recipes (name, meal_type, protein, cuisine, time_req) VALUES ("{meal_name}", "{meal_type}", "{protein}", "{cuisine}", "{time_req}")'
    cursor.execute(query_string)
    connection.commit()

def fetch_all():
    query_string = "SELECT * FROM recipes"
    results = cursor.execute(query_string)
    connection.commit()
    return results.fetchall()