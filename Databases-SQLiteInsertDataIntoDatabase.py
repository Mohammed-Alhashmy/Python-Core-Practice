import sqlite3

dataBase = sqlite3.connect("app.db")

cursor = dataBase.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS skill (name TEXT, progress INTEGER, user_id INTEGER)")

#####################

# cursor.execute("insert into users(user_id, name) values(1, 'Mohammed')")
# cursor.execute("insert into users(user_id, name) values(2, 'Alex')")
# cursor.execute("insert into users(user_id, name) values(3, 'Alaa')")
# cursor.execute("insert into users(user_id, name) values(4, 'Ali')")


my_list = ["Ahmed", "Ali", "Alex", "Dune", "Mark", "Steve"]

for key, users in enumerate(my_list):

    cursor.execute(f"insert into users(user_id, name) values({key + 1}, '{users}')")


dataBase.commit()

dataBase.close()