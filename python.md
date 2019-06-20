# python

## Util

* globals(): dic => get class by classname

```python
product = globals()["Product"]("ProductName")
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

```pythonv
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