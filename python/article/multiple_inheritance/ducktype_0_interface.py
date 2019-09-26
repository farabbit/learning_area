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
"""
a shark can hunt, and a shark can swim
"""
