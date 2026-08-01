import sqlite3


def get_all_data():

    try:
        db = sqlite3.connect("Test.db")


        print("Connected To Data Base Successfully")

        cr = db.cursor()

        cr.execute("select * from users")

        results = cr.fetchall()

        print(f"Your Data Rows is : {len(results)}")

        print("Showing Data : ")

        for row in results:

            print(f"UserID-> {row[0]}", end=" ")
            print(f"Username-> {row[1]}")
        
    except sqlite3.Error as er:
        print(f"Error Reading data {er}")


    finally:


        if (db):
            db.close()

            print("Connection To Database Is Closed")

        




get_all_data()