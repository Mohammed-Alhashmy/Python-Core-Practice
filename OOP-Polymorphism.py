class A:

    def do_something(self):
        print("This is From Class A")

        raise NotImplemented("Derived class Must Implements This Method")
    
class B(A):

    def do_something(self):
            print("This is From Class b")

    pass

class C(A): 
    pass

my_printer = B()

my_printer.do_something()