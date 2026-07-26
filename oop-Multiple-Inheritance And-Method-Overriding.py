class BaseOne:
    def __init__(self):

        print("Message : Base One")

    def func_one(self):

        print("Func One")

class BaseTwo:
    def __init__(self):

        print("Message : Base Two")

    def func_two(self):

        print("Func Two")

class Derived(BaseOne, BaseTwo):
    pass


var = Derived()

var.func_one()
var.func_two()



class Base:

    def __init__(self):

        print("This is from main base ")

    def func_base(self):
    
            print("Func One")



class DerivedOne(Base):
    pass

class DerivedTwo(DerivedOne):
    pass


myvariable = DerivedTwo()

myvariable.func_base()

