# python advanced

## Utilities

```python
for i in sorted(collection): pass
for i in reversed(collection): pass
'{:<3}|{:^3}|{:>3}'.format('a','b','c') # 'a  | b |  c'
```

## syntactic sugar 语法糖

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

## data structure 数据结构

### tuple

```python
a=1, # a=(1,)
# tuple unpacking
a,b=1,2 # (a,b)=(1,2)
a,(b,c)=1,(2,3) # a=1,b=2,c=3
# uncertain tuple
a,b,*rest=range(5) # a=0,b=1,rest=(2,3,4)
a,*resc,b=range(5) # a=0,rest=(1,2,3),b=4
```

### collections.namedtuple 具名元组

> Used to build object that need no method and have limited attributes.

```python
import collections
# Card here is a class now
Card = collections.namedtuple('Card', ['rank', 'suit']) # two parameters, Name and Fields
Card = collections.namedtuple('Card','rank suit') # also
DiamondsJ = Card('J', 'Diamonds')
DiamondsJ._fields # ('rank', 'suit') Cards._fields also possible
DiamondsJ._asdict() # ('rank', 'suit')
```

## Special methods 特殊方法

```python
class Deck:
    def __init__(self): self._cards=[suit+str(rank) for rank in range(10) for suit in 'ABCD' ]
    def __repr__(self): return ','.join(_cards)
    def __len__(self): return len(self._cards)
    def __getitem__(self, index): return self._cards[index] # iterable -> enables: in, slice [::], reversed()
    def __call__(self,index): return self[index] # deck(9)
    def __setitem__(self,key,value): pass # deck['D2'] = Card('Diamond','2')
    def __getitem__(self,key): pass # print(deck['D2'])
    def __delitem__(self,key): pass # del deck['D2']
    def __iter__(self): pass #
```

## random

random.choice(collection)

```python
import random
numbers=[i for i in range(10)]
random.choice(numbers) # will return a random index of numbers
```
