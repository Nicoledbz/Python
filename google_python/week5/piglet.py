# class piglet:
    # def speak(self):
        # print("oink oink")

# hamlet = piglet()
# hamlet.speak()
#======================================================================================================

#class piglet:
 #   name = "piglet"
  #  def speak(self):
   #     print("oink! I'm {}! oink!".format(self.name))

#hamlet = piglet()
#hamlet.name = "Hamlet"
#hamlet.speak()

#petunia = piglet()
#petunia.name = "petunia"
#petunia.speak()
#===========================================================================================================
#class piglet:
 #   years =0
  #  def pig_years(self):
   #     return self.years * 18

#piggy = piglet()
#print(piggy.pig_years())

#piggy.years = 2
#print(piggy.pig_years())
#===========================================================================================================
# OK, now it’s your turn! Have a go at writing methods for a class.

# Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).

#class Dog:
 # years = 0
 # __
    
#fido=Dog()
#fido.years=3
#print(fido.dog_years())
###################################################################################################################

class Animal:
  sound = ""
  def __init__(self, name):
      self.name = name
  def speak(self):
      print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class piglet(Animal):
    sound = "oink!"

hamlet = piglet("hamlet")
hamlet.speak()

class cow(Animal):
  sound = "Mooooo"

milky = cow("Milky White")
milky.speak()

##########################################################################################################
     
#Let’s create a new class together and inherit from it. 
# Below we have a base class called Clothing. Together, let’s create a 
# second class, called Shirt, that inherits methods from the Clothing class. 
# Fill in the blanks to make it work properly.

class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.___,self.___))
			
class Shirt(___):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()