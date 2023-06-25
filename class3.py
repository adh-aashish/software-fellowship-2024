class Animal:

    def get_attributes(self):
        print("Name: ",self.name) 
        print("Colour: ",self.colour)

    def set_name(self, name):
        self.name = name

# object creattion
animal_object = Animal()

# attributes assignment
animal_object.name = "Cloud"
animal_object.colour = "Brown"

#method call
animal_object.get_attributes()

#setter method
animal_object.set_name("Badal")


animal_object.get_attributes()