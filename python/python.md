# python

## Util

* globals(): dic => get class by classname

```python
product = globals()["Product"]("ProductName")
```

## File I/O

```python
rf = open(FileName, mode='r')

rf.read() # read all
rf.readLine() # read one line
rf.readLines() # read all lines as a list

wf = open(FileName, mode='w') # if FileName not exit, auto create a new one. mode can also be 'a'
wf.write()
wf.writeLine()
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

### QUEUE

```python

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