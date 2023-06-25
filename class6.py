class Animal:

    def eat(self):
        print("I can eat")

# inherit from Animal


class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)


# create an object of the subclass
labrador = Dog()

# inheritance of parent method
labrador.eat()

labrador.name = "Badal"
# call subclass method
labrador.display()
