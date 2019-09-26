""" duck type using """
print("duck type that implemented 'interface'")

class Animal:
    def __init__(self):
        self.species = self.__class__.__name__

    def __str__(self): return "I'm a %s" % self.species

class Hunter:
    def hunt(self): pass

class Swimmer:
    def swim(self): pass

class Shark(Animal):
    def hunt(self): return "a shark can hunt"

    def swim(self): return "a shark can swim"

    def __str__(self): return super().__str__ + " and I can hunt and swim"

def intro(hunterType, swimmerType):
    print("%s, and %s" % (hunterType().hunt(), swimmerType().swim()))

intro(Shark, Shark)

""" code reuse """
print("\ncode reuse")

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


""" duck base type have constructor or property """

class Animal:
    def __init__(self):
        self.species = self.__class__.__name__
        print("Initing an Animal")

    def __str__(self): return "I'm a %s" % self.species

class Hunter(Animal):
    def __init__(self, prayList):
        super().__init__()

        self.prayList

    def hunt(self):
        print("a %s can hunt %s" % (self.species, " and ".join(prayList)))

class Swimmer(Animal):
    def __init__(self, area):
        super().__init__()

        self.area = area

    def swim(self):
        print("a %s swims in %s" % (self.species, self.area))

class Shark:
    def __init__(self):
        Hunter.__init__(self, ["Tunas", "Saury"])
        Swimmer.__init__(self, "Pacific Ocean")

    def swim(self):
        Swimmer.swim(self)

    def hunt(self):
        Hunter.hunt(self)

s = Shark()
s.swim()
s.hunt()
