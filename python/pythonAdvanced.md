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

duck type: classes do not need to interited from a perennt class 

```python
class Deck:
    def __init__(self): self._cards=[suit+str(rank) for rank in range(10) for suit in 'ABCD' ]
    def __repr__(self): return ','.join(_cards)
    def __len__(self): return len(self._cards)
    def __getitem__(self, index): return self._cards[index] # iterable -> enables: in, slice [::], reversed(), sorted(), ...
    def __call__(self,index): return self[index] # deck(9)
    def __setitem__(self,key,value): pass # deck['D2'] = Card('Diamond','2')
    def __getitem__(self,key): pass # print(deck['D2'])
    def __delitem__(self,key): pass # del deck['D2']
    def __iter__(self): pass # TODO
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

    def setStrategy(self, strategy): self.strategy = strategy

    def executeStrategy(self):
        return self.strategy(self)
# find all strategies using globals()
strategies = (globals()[name] for name in globals()  if = name.startswith('Strategy'))
```

TODO: see DesignPatterns/Strategy.py

### command pattern 命令模式

> Behaviour pattern 行为型模式，请求以命令的形式包裹在对象中，并传给调用对象  
> 调用对象寻找可以处理该命令的合适对象，并令其执行

TODO: see /DesignPatterns/Command.py

## Decorator 装饰器

---

> 'tag' functions to enhance their behavior  
> understand **Closure** before learning Decorator

definition:
> Decorator is callable objects takes a function as its parameter (the parameter is the function which been decorated)

### basic decorator demo

```python
def decorator(func): return func

@decorator
def taget(): print("running target()")
# same effect as
def taget(): print("running target()")
target = decorator(target)
```

> The target function been decorated will **be replaced by** decorator  
> decorator will be **executed once** the function been **defined**

### use decorator to enhance strategy pattern

> registe the strategy once it has been defined

TODO: see /DesignPatterns/Strategy.py

### variable scope 变量作用域

1. 函数内可以直接使用全局变量
2. 函数内若给与某全局变量名称相同的变量赋值，该变量会变为局部变量
3. 只要函数内部改变变量的值，编译时便会认为在本函数中改变了为局部变量
4. 作为参数传递的全局变量在函数内是局部变量
5. 若要在函数内改变全局变量的值，使用global关键字修饰

### Closure 闭包

TODO: 复习闭包

> 指延展了作用于的函数，可访问定义体之外的**非全局变量**

```python
def make_average(): # higher-order function that returns a function
    series = [] # free variable, can save status
    def averager(new_value): # this is a closure, it can access the list series
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager

avg=make_averate()
avg(10) # 10
avg(12) # 11
# python stores local var and free var in __code__( __code__ is compiled function definition)
avg.__code__.co_varnames # ('new_value', 'total')
avg.__code__.co_freevars # ('series',)
# __closure__ is a list that reflects every variable name in __code__.co_freevars
avg.__closure__ # (<cell at 0x107a44f78: list object at 0x107a91a48>,)
avg.__closure__[0].cell_contents # [10, 12]
```

### Nonlocal annoncement

```python
def make_averager():
    count = 0; total = 0
    def averager(new_value):
        nonlocal count, total # if no nonlocal here, count & total will be compiled as local variable
        count += 1
        total += new_value
        return total / count
    return averager
```

### decorator

```python
import operator
import functools

def OperatorForDisplay(operatorFunc):
    # can add decorator functools.wraps(func) to support keyword parameters
    def Display(*nums): # not support **kwargs in normal closure
        print("The", operatorFunc.__name__,"result of", *nums, "is", operatorFunc(*nums))
    return Display

@OperatorForDisplay
def Add(*nums): return sum(nums)

@OperatorForDisplay
def Mul(*nums): return functools.reduce(operator.mul, nums)

# function changed after decorated by OperatorForDisplay
Add(2,3,4) # The Add result of 2 3 4 is 9
Mul(2,3,4) # The Mul result of 2 3 4 is 24
```

### decorator in std lib

* @functools.lru_cache(), cache function result
* @functools.singledispatch, 将函数变为 *single dispatch generic function 单分派泛函数*

#### @lru_cache()

cache function result, Least Recent Used, 缓存函数结果，若再有使用相同参数的调用，将直接使用缓存结果，最久未使用的缓存将被清除
> 用于修饰无状态的函数，或需要慢速递归的函数如递归生成斐波那契数列，可大幅度缩减所需时间  
> 被修饰的函数的参数必须hashable  
> maxsize最好是2的幂以获得最佳性能，typed=True时不同类型的参数将分别储存，如1与1.0

```python
import functools

@functools.lru_cache()
def fibonacci(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)
```

#### @singledispatch

将函数变为 *single dispatch generic function 单分派泛函数* -> partial function?
> 分派函数指的是，根据函数中参数的不同，使用不同的功能函数来处理，单分派：根据单一参数进行分派  
> 用if-elif-else调用专门函数 -> 笨拙，耦合紧密，不利于模块扩展
> 使用泛函数会使其看起来像override

```python
import functools
from collections import abc;import numbers

@functools.singledispatch # decorated by singledispatch will receive when don't match other register
def displayObject(obj): print(obj, "is a base object")

@displayObject.register(str) # register str type for displayObject, kinda like override
def _(text): print(text, "is a str")

@displayObject.register(numbers.Integral)
def _(n): print(n, "is a integer")

@displayObject.register(abc.MutableSequence)
def _(seq): print(seq, "is a mutable sequence")

displayObject((1,2)) # (1, 2) is a base object
displayObject("hello") # hello is a str
displayObject(123) # 123 is a integer
displayObject([1,2]) # [1, 2] is a mutable sequence
```

### decorator with parameter

> In conception filed, a decorator with parameter isa 'decorator factory' instead of a 'decorator'

```python
registory=set
def register(active=True): # this is a decorator factory that returns a decorator
    def regist(func):
        if active: registory.add(func)
        else: regist.discard(func)
    return regist
# if put: @register: register is a function, the decorator will be register
# if put: @register(): register() will return a function, the decorator will be register.regist instead
```

## OOP utilities

---

### Object reference

pass

### Copy & deep copy

copy.copy(obj)
copy.deepcopy(obj)

implement __copy__() and __deep_copy() to customize copy behavior

### Do not use mutable variable as default parameter

exp: HauntedBus

### del

> del will only delete refrence, not object. however, del may cause object been recycled if the refrence is the only remaining refrence.

### weak refrence

weak refrence will not be counted to refrenced number of a object.
object be weak refrenced called 'refrent'

> most used in cache

```python
import weakref
s1="Hello World!"
wref=weakref.ref(s1);print(wref) # Hello World!
del s1; print(wref) # None
```

### WeakValueDictionary

mutable mapping that value is weak refrence of objects

> most used in cache

