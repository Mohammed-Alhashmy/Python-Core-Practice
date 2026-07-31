import sqlite3

db = sqlite3.connect("myApp.db")

db.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")

db.close()