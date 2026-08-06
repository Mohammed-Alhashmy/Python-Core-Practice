import sqlite3

db = sqlite3.connect("AnotherTest.db")

cr = db.cursor()


cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")

cr.execute("CREATE TABLE IF NOT EXISTS skill (name TEXT, progress INTEGER, user_id INTEGER)")

mytup = ("java", "55", 4)

# cr.execute("insert into skill Values(?, ?, ?)", mytup)

cr.execute("select * from skill where user_id not in(1,4)")

results = cr.fetchall()


for row in results:

    print(f"Skill Name => {row[0],}", end= " ")
    print(f"Skill Progress => {row[1]}", end= " ")
    print(f"User_id => {row[2]}")

db.commit()

db.close()

