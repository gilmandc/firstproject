import sqlite3

connection = sqlite3.connect("/home/gilmandc/Projects/firstproject/recipe_book.db")
cursor = connection.cursor()
init_script = "CREATE TABLE IF NOT EXISTS recipes(recipe_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, meal_type TEXT, protein TEXT, cuisine TEXT, time_req INTEGER)"
cursor.execute(init_script)
cursor.execute("""INSERT INTO recipes (name, meal_type, protein, cuisine, time_req)
VALUES ('burgers', 'lunch', 'beef', 'American', 2)""")
connection.commit()



get_all = "SELECT * FROM recipes"
cursor.execute(get_all)






results = cursor.fetchall()
cursor.close()
connection.close()
print(results)
