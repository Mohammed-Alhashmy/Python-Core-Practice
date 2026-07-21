class Member:
    
    User_num = 0

    @classmethod
    def show_user_count(cls):
        print(f"We Have {cls.User_num} User in The App ")

    @staticmethod
    def sayHi():
        print("Hello World How Are You")

    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        Member.User_num +=1
        



member_One = Member("Mohammed", "Sadiq", "Haider", "male")
member_Two = Member("Mona", "Ahmed", "Kira", "female")

Member.show_user_count()

Member.sayHi()