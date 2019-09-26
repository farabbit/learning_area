class Animal:
    def __init__(self):
        self.species = self.__class__.__name__

    def __str__(self): return "I'm a %s" % self.species

class Hunter(Animal):
    def hunt(self):
        print("a %s can hunt" % self.species)

    def smash(self):
        print("when hunting, a %s will smash its prey" % self.species, end="")

class Tiger(Hunter): # inherit explictly
    # case 1: no need to define hunt() again

    def smash(self): # case 2
        super().smash() # code reuse
        print(" using teeth and claws") # feature

class Shark(Animal): # duck type
    def hunt(self): # case 1
        Hunter.hunt(self)

    def smash(self): # case 2
        Hunter.smash(self) # code reuse
        print(" using its teeth") # feature

Tiger().hunt()
Tiger().smash()
Shark().hunt()
Shark().smash()
"""
a Tiger can hunt
when hunting, a Tiger will smash its prey using teeth and claws
a Shark can hunt
when hunting, a Shark will smash its prey using its teeth
"""
