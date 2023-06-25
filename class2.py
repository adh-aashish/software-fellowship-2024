class Animal:

    def get_attributes(self):
        print("Name: ",self.name) 
        print("Colour: ",self.colour)
        

# object creattion
animal_object = Animal()

# attributes assignment
animal_object.name = "Cloud"
animal_object.colour = "Brown"

#method call
animal_object.get_attributes()