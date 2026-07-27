class Member:
    def __init__(self, name):

        self.__name = name

    def sayHello(self):

        return f"Hello how are you Mr.{self.__name}"

    def get_name(self):

        return self.__name

    def set_name(self, new_name):

        self.__name = new_name

test = Member("Dune")

# print(test._Member__name)

print(test.get_name())

test.set_name("Alex")

print(test.get_name())


