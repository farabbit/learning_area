# python中的多继承

* 鸭子类型的多态性
  * 实现“鸭子接口”的鸭子类型
  * 在鸭子类型中复用鸭子基类代码
* 显式多继承
* super()的工作原理
  * 类的```__mro__```属性
* 基类具有带参构造函数多继承出现的问题
* 最佳实践 - 如何优雅的实现多继承

## 鸭子类型

---

> 当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么它就可以被称为鸭子。

### 实现鸭子“接口”的鸭子类型

鸭子类型不需要显式地继承基类，而可以通过隐式的多继承来实现一定程度上的多态性。我们不妨把鸭子叫做鸭子基类，把看起来像鸭子的鸟类叫做伪鸭子类（实际上这种说法有一些tricky，虽然称作伪鸭子，但其实它就是鸭子，而且我们还把伪鸭子叫做鸭子类型）

我们来看下面这个经典的菱形继承例子

```python
class Animal:
    def __init__(self):
        self.species = self.__class__.__name__

    def __str__(self): return "I'm a %s" % self.species

class Hunter:
    def hunt(self): pass

class Swimmer:
    def swim(self): pass

class Shark(Animal): # duck type of Hunter and Swimmer
    def hunt(self): print("a shark can hunt")

    def swim(self): print("a shark can swim")

    def __str__(self): return super().__str__ + " and I can hunt and swim"

def intro(hunterType, swimmerType): # want to receive Hunter and swimmer
    hunterType().hunt()
    print(", and", end="")
    swimmerType().swim()

intro(Shark, Shark) # Shark is both hunter and swimmer
# a shark can hunt, and a shark can swim
```

在这个例子中，Hunter和Swimmer类是鸭子，Shark类则是伪鸭子，虽然没有直接继承，但Shark具有Hunter与Swimmer的一切功能（当然，也可以只实现一部分功能）

此时你可能发现了，虽然使用鸭子类型一定程度上实现了多态，但此时Hunter与Swimer类更像是只提供抽象方法的接口类，如果hunt()与swim()方法有具体实现的话，Shark类的对应方法需要显式调用这两个基类方法才能做到代码复用

### 在鸭子类型中复用基类代码

如果需要鸭子类要承担一部分功能实现，则有以下两种情况

1. 鸭子类中有具体实现，伪鸭子类中想要复用这个实现
2. 鸭子类中有具体实现，伪鸭子类中想要复用这个实现的代码，并加上自己的独特功能

对于这两种情形，我们可以将其与显式继承做对比：

```python
class Animal:
    def __init__(self):
        self.species = self.__class__.__name__

    def __str__(self): return "I'm a %s" % self.species

class Hunter(Animal):
    def hunt(self):
        print("a %s can hunt" % self.species)

    def smash(self):
        print("when hunting, a %s will smash its prey" % self.species, end="")

class Tiger(Hunter): # inherit Hunter explictly
    # case 1: no need to define hunt() again

    def smash(self): # case 2
        super().smash() # code reuse
        print(" using teeth and claws") # feature

class Shark: # duck type of Hunter
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
```

在情形1中，显式继承不需要再定义这个方法并实现实现，而鸭子类型需要定义此方法，把基类的这个方法当作类方法（class method）调用，并把自身传入

对于case 2，显式继承调用```super().__smash__()```来复用基类代码，鸭子类型的做法则与情形1没什么两样

## 基类带属性或带构造函数的多继承

在上面的例子中，基类都不带有属性，提供的只是方法的集合，而若鸭子基类有内置属性，或构造函数带有参数，此时鸭子类型的地位就很尴尬了

```python
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
        print("a %s can hunt %s" % (self.species, " and ".join(prayLis)))

class Swimmer(Animal):
    def __init__(self, area):
        super().__init__()

        self.area = area

    def swim(self):
        print("a %s swims in %s" % (self.species, self.area))
```

到目前为止一切都看上去似乎都很合理，Hunter和Swimer是Animal，所以显式继承了Animal类，在它们的构造函数中都使用了```super().__init__()```来调用Animal的构造函数。

在之前的例子中，鸭子基类没有构造函数，伪鸭子类继承Animal直接使用它的构造函数没什么问题，但如果鸭子基类中有构造函数，此时

如果此时使用鸭子类型，若要获得Swimmer和Hunter的的属性，必须复用它们的构造函数，但显然```super().__init__()```会被调用两次，更糟糕的是，我们的Shark也是一个Animal，如果要像之前的例子显式继承Animal类的话，Animal的构造函数会被调用三次：

```python
class Shark:
    def __init__(self):
        Hunter.__init__(self, ["Tunas", "Saury"])
        Swimmer.__init__(self, "Pacific Ocean")

    def swim(self):
        Swimmer.swim(self)

    def hunt(self):
        Hunter.hunt(self)

Shark()
```

Hunter()

> Best Practice: 鸭子基类最好只是抽象接口

## super()的工作原理

```__mro__```

## 显式多继承

TODO

## 最佳实践

```python
import functools

def initMonitor(_type):
    def initWrapper(initFunc):
        @functools.wraps(initFunc)
        def __init(*args, **kwargs):
            print("enter %s.__init__()" % _type)
            initFunc(*args, **kwargs)
            print("exit %s.__init__()" % _type)
        return __init
    return initWrapper


class Animal:
    @initMonitor("Animal")
    def __init__(self, name="Nemo"):
        self.name=name
        self.species = self.__class__.__name__

    def __str__(self):
        return "I'm a %s, my name is %s" % (self.species, self.name)

class Hunter(Animal):
    @initMonitor("Hunter")
    def __init__(self, prayList=None, **kwargs):
        super().__init__(self, **kwargs)
        self.prayList = prayList

    def hunt(self):
        print("a %s can hunt %s" % (self.species, " and ".join(prayLis)))

class Swimmer(Animal):
    @initMonitor("Swimmer")
    def __init__(self, area, **kwargs):
        super().__init__(**kwargs)
        self.area = area

    def swim(self):
        print("a %s swims in %s" % (self.species, self.area))

class Shark
```