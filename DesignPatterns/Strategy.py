import abc

""" Traditional way """
# every strategy is as class that inherits base stategy
print("Traditional: ")

class Strategy:
    """ Base Strategy """
    @abc.abstractmethod
    def operation(self, context): pass

# concrate stategies
class StrategyAdd(Strategy):
    def operation(self, context): return context.intA + context.intB
class StrategyMultiple(Strategy):
    def operation(self, context): return context.intA * context.intB

class Context:
    """ class that using Strategy """
    def __init__(self, intA, intB):
        self.intA, self.intB = intA, intB

    def setStrategy(self, strategy):
        self.strategy = strategy

    def executeStrategy(self):
        return self.strategy.operation(self)

context = Context(2, 3)
context.setStrategy(StrategyAdd()) # using add
print("ADD:", context.executeStrategy()) # ADD: 5
context.setStrategy(StrategyMultiple()) # using multiple
print("MUL:", context.executeStrategy()) # MUL: 6


""" Restruct using functional programming """
# concrete stragegies had no internal status -> performanced like functions
print("Restructed: ")

def StrategyAdd_res(context): return context.intA + context.intB

def StrategyMultiple_res(context): return context.intA * context.intB

class Context_res:
    """ class that using Strategy """
    def __init__(self, intA, intB):
        self.intA, self.intB = intA, intB

    def setStrategy(self, strategy): # syntax keeps the same but strategy here is function now, not a class
        self.strategy = strategy

    def executeStrategy(self):
        return self.strategy(self)

context_res = Context_res(2, 3)
context_res.setStrategy(StrategyAdd_res) # using add
print("ADD:", context_res.executeStrategy()) # ADD: 5
context_res.setStrategy(StrategyMultiple_res) # using multiple
print("MUL:", context_res.executeStrategy()) # MUL: 6


""" best strategy """
# additional functionalities
print("Choose best strategy among all: ")

strategies = (StrategyAdd_res,StrategyMultiple_res)

def bestStrategy(context):
    """ choose a best strategy from strategy list """
    return max(strategy(context) for strategy in strategies)

print("MAX(ADD(2,3), MUL(2,3)):", bestStrategy(Context_res(2,3))) # 6


""" Find all strategies """
# using globals(): returns every global variable that in current module (module that defines that function/method)

strategies = (globals()[name] for name in globals()  if name.endswith('_res') and name.startswith('Strategy'))
print(list(strategies)) # [StrategyAdd_res,StrategyMultiple_res]

"""out: 
Traditional
ADD: 5
MUL: 6
Restructed:
ADD: 5
MUL: 6
Choose strategy among all
MAX(ADD(2,3), MUL(2,3)): 6
[<function StrategyAdd_res at 0x00000299A4A33E18>, <function StrategyMultiple_res at 0x00000299A4D5B378>]
"""
