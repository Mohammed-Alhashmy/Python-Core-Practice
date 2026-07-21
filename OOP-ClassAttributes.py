class Member:

    not_allowed_names = ["God", "dumb", "dog", "shit"]
    
    users_number = 0

    def __init__(self, firstname, secname, lastname):
        
        self.fName = firstname
        
        self.sName = secname

        self.lName = lastname

        Member.users_number += 1
    
    def full_name(self):
        
        if self.fName in Member.not_allowed_names:
            
            raise ValueError("You can Not Take This Name Please Try another One .")
        else:

            return f"{self.fName} {self.sName} {self.lName}"
        
    def delete_user(self):

        Member.users_number -=1
        
        return f"User {self.fName} has been deleted "

member_One = Member("mahmoud", "ali", "ahmed")
member_two = Member("jassim", "mahmod", "dal")
member_three = Member("mona", "ahmed", "mahmoud")




print(member_One.full_name())
print(Member.users_number)
print(member_three.delete_user())
print(Member.users_number)
