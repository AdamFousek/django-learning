class Dog():
    # class attribute
    somethin = "hello"

    def __init__(self, breed):
        self.breed = breed
        pass

    def set_breed(self, new_breed):
        self.breed = new_breed


my_dog = Dog("Lab")

# print(my_dog.breed)


class Animal():

    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")


dog = Dog()
