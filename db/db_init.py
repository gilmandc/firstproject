import sqlite3

connection = sqlite3.connect("/home/daniel/pythonprojects/firstproject/recipe_book.db")
cursor = connection.cursor()
init_script = "CREATE TABLE IF NOT EXISTS recipes(recipe_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, meal_type TEXT, protein TEXT, cuisine TEXT, time_req INTEGER)"
cursor.execute(init_script)
connection.commit()










results = cursor.fetchall()
cursor.close()
connection.close()
print(results)
