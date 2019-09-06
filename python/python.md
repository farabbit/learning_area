# PYTHON

## Util

* globals(): dic => get class by classname

```python
product = globals()["Product"]("ProductName")
```

## File I/O

mode

* r: read
* w: write
* a: append
* b: read/write binaries

```python
rf = open(FileName, mode='r')

rf.read() # read all
rf.readLine() # read one line
rf.readLines() # read all lines as a list

wf = open(FileName, mode='w') # if FileName not exit, auto create a new one. mode can also be 'a'
wf.write()
wf.writeLine()

rf.close()
wf.close()
```

## python shell

```python
# 1. os.system(): return status code
status=os.system('pwd') # os.system will return runing result 0=OK, 256=COMMAND NOT FOUND
# 2. os.popen(): run shell return std output
output=os.popen('pwd') # will return file obj
temp=output.readline() # read one line
for temp in output.readlines(): pass # read multiple line
# 3. subprocess.run()
import subprocess
subprocess.getstatusoutput('pwd') # return (status, output)
subprocess.getoutput('pwd')
subprocess.call('pwd') # return status (vary similar to os.system) ---> subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None), if shell=False, options of command must be written seperatly
subprocess.call_all(['pwd','ls'])
subprocess.check_call('pwd') # return status if success, else raise exception ---> subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
subprocess.check_output('pwd') # return output if success, else raise exception
subprocess.Popen(command,shell=True,cwd='/home/dev')
```

## data structure 数据结构

### dict

```python
# create a dict
a = dict(one=1,two=2,three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip['one','two','three'],[1,2,3])
d = dict(['one',1],['two',2],['three',3])
a == b == c == d # True

# dictcomp
country_code = {country:code for code, country in DIAL_CODES} # DIAL_CODES: [(86,'China'),(01,'India')]

# methods
dic.fromkeys(iter, [initial]) # set key as iter, value as initial (optional)
dic.setdefault(key[,defaultValue]) # will return dic[key] no matter key exits or not
```

Other dicts

```python
# collections.defaultdict
ddic = collections.defaultdict(lambda: 'Default') # set default_factory as 'return default'
ddic['D1'] # return 'Default'
def __missing__(self,key): self[key]='default';return default
# collections.OrderedDict: iteration order will be sorted
# collections.chainmap: 合并dict
# collections.UserDict：纯python实现，用于用户继承子类化
# types.MappingProxyType: 不可变集合
```

### set

```python
# operators
a|b # aggregation 合集
a&b # intersection 交集
a-b # difference 差集
a^b # 对称差集

e in a # element in set
a<=b # >,>=,<,<=

# frozenset
```

### Sequence

#### tuple

```python
a=1, # a=(1,)
# tuple unpacking
a,b=1,2 # (a,b)=(1,2)
a,(b,c)=1,(2,3) # a=1,b=2,c=3
# uncertain tuple *
a,b,*rest=range(5) # a=0,b=1,rest=(2,3,4)
a,*resc,b=range(5) # a=0,rest=(1,2,3),b=4
```

#### collections.namedtuple 具名元组

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

#### array

```python
from collections import array
from random import random
floats = array('d',(random() for i in range(10**7))) # assign type 'd' to array, and generate 10000000 double
fp=open('floats.bin','wb') # write binary mode
floats.tofile(fp) # serialize numbers in efficient way

floatsRead = array('d').fromfile(fp,'rb') # directly read from file
fp.close
```

#### QUEUE

```python
# collections.deque 双向队列
import collections
dq = collections.deque(range(10), maxlen=10) # maxlen: CANNOT CHANGE, if add more elements on one side, elements on other side will be deleted
dq.rotate(3) # put right 3 to left dq=deque([7,8,9,0,1,2,3,4,5,6], maxlen=10)
dq.rotate(-4) # put left 4 to right dq=deque([4,5,6,7,8,9,0,1,2,3], maxlen=10)
dq.appendleft(-1) # .append defautly put element on the right
dq.extendleft([1,2,3]) # .extend defautly put element on the right

# queue 队列, provide synconized class
# Queue, LifoQueue, PriorityQueue
# if add more elements than maxsize, Queue will be locked until elements be consumed

# multiprocessing.Queue 用于进程间通信
```

## OOP

---

### static method & class method

@classmethod

> 类方法，需要cls参数

```py
class Animal:
    @classmethod
    def AnimalCount(cls): pass
```

@staticmethod

> 不需要用到self时可加，用于增加可读性，不需要cls参数

### interitance

```python
class Animal: pass
class Dog(Animal): pass
```

#### abstract

需要先import abc用于处理抽象

```python
import abc # abstract
```

#### abstract method

```python
class Anmal:
    @abc.abstractmethod
    def eat(): pass # pass is needed, means it will not be implemented right here
```

## relection

```python
ret = getattr(obj, 'func')
hasattr(obj, 'func')
setattr(obj, 'func')
delattr(obj, 'func')
```
