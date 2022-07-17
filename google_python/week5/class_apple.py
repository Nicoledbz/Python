class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold)
# ###################################################################################################################

class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    ___
    print("Hello! My name is {name}.".format(name=self.name)) 

help(___)