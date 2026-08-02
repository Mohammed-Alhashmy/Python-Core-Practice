import sqlite3

db = sqlite3.connect("Test.db")

cr = db.cursor()

cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")

cr.execute("update users set name = 'jack' where user_id = 1")
cr.execute("update users set name = 'drag' where user_id = 2")
cr.execute("update users set name = 'mike' where user_id = 3")


cr.execute("delete from users where user_id = 3")

cr.execute("select * from users")

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

db.commit()

db.close()