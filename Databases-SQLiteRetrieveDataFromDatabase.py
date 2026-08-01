import sqlite3

db = sqlite3.connect("Test.db")

cr = db.cursor()

cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")

# cr.execute("insert into users(user_id, name) values(1, 'Mohammed')")
# cr.execute("insert into users(user_id, name) values(2, 'alex')")
# cr.execute("insert into users(user_id, name) values(3, 'dune')")

cr.execute("select user_id, name from users")

# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchall())
print(cr.fetchmany(2))


db.commit()