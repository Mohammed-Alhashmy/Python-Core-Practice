class food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"{self.name} Is Created By the (Base class)")

    def eat(self):
        print("Eat From (Base class)")

class Apple(food):
    def __init__(self, price, name, amount):

        super().__init__(price, name)
        self.amount = amount

        print(f"{self.price} from (derived class) and {self.name} from (derived class) and the amount is : {self.amount}")


#food_one = food("f")
food_two = Apple("Pizza",150,4)
