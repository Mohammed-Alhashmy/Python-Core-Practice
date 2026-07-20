
class Member :
    users_count = 0
    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        Member.users_count += 1

    def full_name(self):

        return f"{self.fname} {self.mname} {self.lname}"
    
    def say_hello(self):
        
        if self.gender == "male" :

            return f"Hello Mr.{self.fname}"
        
        elif self.gender == "female": 

            return f"Hello Miss.{self.fname}"
        
        else:
            return f"Hello {self.fname}"
            
    def get_all_info(self):

        return f"{self.say_hello()} , Your full name is : {self.full_name()}"
    
member_One = Member("Mohammed", "Sadiq", "Haider", "male")
member_Two = Member("Mona", "Ahmed", "Kira", "female")
member_Three = Member("Ali", "Omer", "Zaki", "male")

# print(member_Two.full_name())
# print(member_Two.say_hello())
print(f"Users Count After: {Member.users_count}")
print(member_One.get_all_info())