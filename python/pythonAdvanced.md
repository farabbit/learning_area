# python advanced

Category

* Utilities
* Functional programming
* Syntactic sugar
* Multi thread *TODO*
* special methods

## Utilities

---

```python
# format
'{:<3}|{:^3}|{:>3}'.format('a','b','c') # 'a  | b |  c'

# sorted, reversed, list.sort, max, min
for i in sorted(collection,comp=None,key=None,reverse=False): pass # key here can be a function that get 1 key param for sort， comp here takes 2 param for compare
for i in reversed(collection, comp, key, reverse): pass
sorted(['2','3',1],key=int) # [1,'2','3']

# map, filter, reduce
map(func,iter) # = func(i) for i in iter
filter(func,iter) # = i for i in iter if func(i)
functools.reduce(func,iter) # func takes 2 params, reduce first take 2 var from iter, and then takes result of prev round and 1 var from iter at next round

# random
import random
numbers=[i for i in range(10)]
random.choice(numbers) # will return a random index of numbers
```

## syntactic sugar 语法糖

---

### List Comprehension 列表推导 & generator expression

```python
# Listcomps
digits = [i for i in range(10)]
cards=[suit+str(rank) for suit in 'ABCD' for rank in range(10)]

# Genexps
digits= (i for i in range(10)) # type <generator>
# if genexps is the only parameter of a funcion, do not need () around
```

### slice 切片

```python
letters='abcdefg'
letters[:3]
letters[3:]
letters[::2]
letters[::-1]
letters[:-1]

DigitList=list(range(10)) # 0,1,2,3,4,5,6,7,8,9
DigitList[2:5]=[30] # 0,1,30,5,6,7,8,9
del DigitList[2:5] # 0,1,7,8,9
```

## Special methods 特殊方法

---

```python
class Deck:
    def __init__(self): self._cards=[suit+str(rank) for rank in range(10) for suit in 'ABCD' ]
    def __repr__(self): return ','.join(_cards)
    def __len__(self): return len(self._cards)
    def __getitem__(self, index): return self._cards[index] # iterable -> enables: in, slice [::], reversed(), sorted()
    def __call__(self,index): return self[index] # deck(9)
    def __setitem__(self,key,value): pass # deck['D2'] = Card('Diamond','2')
    def __getitem__(self,key): pass # print(deck['D2'])
    def __delitem__(self,key): pass # del deck['D2']
    def __iter__(self): pass #
```

## functional programming 函数式编程

---

FluentPython 第五章

> higher-order function 高阶函数 = 参数列表有函数参数，或返回值为函数

### functional programming

> Usually use functions instead of operators, eg: use sum() instead of +  
> solution: lambda expression, or operator module

#### operator module

```python
import operator
# mul, itemgetter, attrgetter
operator.mul(x,y) # = lambda x,y:x*y
operator.itemgetter(n) # = lambda seq:seq[n], multiple argument: operator.itemgetter(n,n+1) = lambda seq:(seq[n],seq(n+1))
operator.attrgetter('attr') # = lambda obj:obj.attr, same as itemgetter

# **operator.methodcaller**
hiphenate = operator.methodcaller('replace',' ','-') # will create a method
hiphenate('Hello World!') # Hello-World! = 'Hello World!'.replace(' ', '-')
```

#### functools.partial 用以冻结(固定)参数/

functools 提供一系列高阶函数，如reduce, partial, partialmethod
> functools.partial: 用于partial application部分应用一个函数，固定参数

```python
triple = partial(mul,3) # freeze first param as a new method triple
triple(7) # 21 = mul(3,7)
list(map(partial(mul,3), range(1,10)))
```

### lambda expression 匿名函数

> most used on param list

```python
lambda x:ord(x) # params : sentence (output of lastline will be returned)
```

### user defined callable type 用户定义可调用对象

```python
# __call__ makes instance callable
class BingoCage:
    def __init__(self): pass
    def pick(self): pass
    def __call__(self): return self.pick()
BingoCage()() # BingoCage is instance, when __call__ defined, it becomes callable
callable(BingoCage) # True
```

> 装饰器、可调用类型可能需要在多次调用间“备忘”，或使用闭包

### function introspection 函数内省

```python
func.__defaults__ # saves defaulted params
func.__code__ # a code obj
func.__code__.co_varnames # saves both params and local vars ('text', 'max_len', 'end', 'space_before', 'space_after')
func.__code__.co_argcount # 2 -> param
```

inspect module

```python
import inspect
sig = signature(clip) # clip is the instance that to be introspected, sig is Signature obj
str(sig) # '(text, max_len=80)'
for name, param in sig.parameters.items(): # items(): ((name, inspect.Parameter)...)
    print(param.kind, ':', name, '=', param.default)
'''
POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
POSITIONAL_OR_KEYWORD : max_len = 80
'''
```

### annotation 注解

```python
# 参数名:注解，常用class或str，函数注解 参数列表->注解
def clip(text:str, max_len:'int > 0'=80) -> str: pass
# 注解不做任何处理，只会存在dict: __annotations__中 （return键保存返回值注解）
# inspect.Signature也可提取注解
```

## Design Patterns 设计模式

---

> design patterns using functions as first-order obejct 使用作为一等对象的函数以简化设计模式

### strategy pattern 策略模式

> Behaviour pattern 行为型模式，类的行为、算法可在运行时更改  
> strategy对象, context对象, strategy对象改变context对象的执行算法, 使得算法独立于用户类

```python
# strategy
def StrategyAdd_res(context): return context.intA + context.intB
# Context
class Context_res:
    """ class that using Strategy """
    def __init__(self, intA, intB): self.intA, self.intB = intA, intB

    def setStrategy(self, strategy):
        self.strategy = strategy

    def executeStrategy(self):
        return self.strategy(self)
# find all strategies using globals()
strategies = (globals()[name] for name in globals()  if = name.startswith('Strategy'))
```

TODO: see DesignPatterns/Strategy.py

## multithread

two ways to pack thread

* function -> _thread.start_new_thread(function, args[, kwargs])
* class -> threading

### threading module

include all functionalities of _thread, have more functions

```python
threading.currentThread() # return current thread variable
threading.enumerate() # return a list of all running thread
threading.activeCount() # return running thread count
```

### thread class

```python
# directly use Thread class
T1 = threading.Thread(target=Method, args=(),kwargs={})
T1.start()
# inherit Thread class
class T2(Threading.thread):
    def run(self): pass
.run() # thread activities, DO NOT NEED TO explicitly call
.start() # start thread, WILL CALL .RUN()
.join([time]) # ???
.isAlive()
.getName()
.setName()
```
