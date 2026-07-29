class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):

        return f"Hello Mr. {self.name}"
    @property
    def age_in_days(self):

        return self.age * 356

test = Member("Mohammed", 21)


print(test.name)
print(test.age)

print(test.sayHello())
print(test.age_in_days())
print(test.age_in_days)