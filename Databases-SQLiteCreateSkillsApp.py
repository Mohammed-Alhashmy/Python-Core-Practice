import sqlite3

db = sqlite3.connect("myApp.db")

cr = db.cursor()


#after make changes close method
def commit_and_closed():

    db.commit()
    db.close()

    print("Connection To DataBase Closed. ")


uid = 1




input_message = """
What Do You Wnat To Do ?
's' -> Show All Skills
'a' -> Add New Skill
'd' -> Delete A Skill
'u' -> Update Skill Progress 
'q' -> Quit App 

Choose Now : 
"""


user_input = input(input_message).lower().strip()

command_list = ["s", "a", "d", "u", "q"]

#Define methods
def show_skills():

    print("Show Skills")

    commit_and_closed()

def add_new_skill():

    sk_name = input("Please Enter Your New Skill : ").capitalize().strip()

    prog = input("Please Enter Your Progress : ").strip()

    cr.execute(f"insert into skills(name, progress, user_id) values('{sk_name}', '{prog}', '{uid}')")

    commit_and_closed()

def delete_skills():

    sk_name = input("Please Enter The Skill You Want to deleted : ").capitalize().strip()

    cr.execute(f"delete from skills where name = '{sk_name}' and user_id = '{uid}'")

    commit_and_closed()

def update_skill_progress():

    print("Update Skill Progress")
    
    commit_and_closed()



#Check if comman exists
if user_input in command_list :

    # print(f"Command confirmed \"{user_input}\" ")

    if user_input == "s":
        show_skills()

    elif user_input == "a":
        add_new_skill()

    elif user_input == "d":
        delete_skills()

    elif user_input == "u":
        update_skill_progress()

    else:
        print("App Is Closed ..")








else:
    print(f"Sorry Comand Not Found {user_input}")