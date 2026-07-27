class Member:
    def __init__(self, name):

        self.name = name #Public 

one = Member("mohammed")

print(one.name)


one = Member("Alhashmy")

print(one.name)



class Member:
    def __init__(self, name):

        self._name = name #Prodected 

one = Member("mohammed")
print(one._name)
one = Member("Alhashmy")
print(one._name)



class Member:
    def __init__(self, name):

        self.__name = name #Private 
    def sayHello(self):

        return f"Hello Mr {self.__name} "

    
one = Member("mohammed")

print(one.sayHello())



