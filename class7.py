class Animal:

    def __init__(self, name, colour):
        self.name = name 
        self.colour = colour

    def get_attributes(self):
        print("Name: ",self.name) 
        print("Colour: ",self.colour)

class Dog(Animal):

    def __init__(self, name, colour, owner):
        super().__init__(name, colour)
        self.owner = owner

    def bark():
        print("Woaf! Woaf!")

# initialization
dog_object = Dog("Badal","Brown","Avishek")

# parent method
dog_object.get_attributes()

# method
dog_object.bark()