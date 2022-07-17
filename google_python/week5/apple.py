#class Apple:
 #   pass

#class Apple:
 #   color = ""
  #  flavor = ""

#jonagold = Apple()
#jonagold.color ="red"
#jonagold.flavor = "sweet"

#print(jonagold.color)
#print(jonagold.flavor)
#print(jonagold.color.upper())

#golden = Apple()
#golden.color = "Yellow"
#golden.flavor = "soft"

#print(golden.flavor)
#print(golden.color)

# class Flower:
#  color = 'unknown'

# rose = Flower()
# rose.color = "red"

# violet = Flower()
# violet.color = "blue"

# this_pun_is_for_you = "Nicole"

# print("Roses are {},".format(rose.color))
# print("violets are {},".format(violet.color))
# print(this_pun_is_for_you) 


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

jonagold = Apple("red", "sweet")
print(jonagold.color)

# Want to see this in action?
 
# In this code, there's a Person class that has an attribute name, which gets set when constructing the object. 
# Fill in the blanks so that 1) when an instance of the class is created, 
# the attribute gets set correctly, and 2) when the greeting() method is called, 
# the greeting states the assigned name.

class Person:
    def __init__(self, name):
        self.name = ___
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return ___ 

# Create a new instance with a name of your choice
some_person = ___  
# Call the greeting method
print(some_person.___)