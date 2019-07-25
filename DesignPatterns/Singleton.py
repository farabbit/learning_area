# 1. 使用模块
# Python的模块是天然的单例模式，模块在第一次导入时，会生成 .pyc 文件，第二次导入时，会直接加载 .pyc 文件，而不会再次执行模块代码。因此，只需把相关的函数和数据定义在一个模块中，就可获得一个单例对象
# # file1
class Singleton1():
    pass
singleton1 = Singleton1()
# # file2
'''
from file1 import singleton1
'''

# 2. 装饰器
def SingletonBase(cls): # 装饰器本质也是一个函数
    _instance = {} # instance dictionary

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

@SingletonBase
class Singleton2:
    pass

# 3. override __new__
class Singleton3:
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

b = Singleton2()
b.display = "123"
c = Singleton2()
c.display = "234"
print(b.display == c.display)

d = Singleton3()
d.display = "123"
e = Singleton3()
e.display = "234"
print(d.display == e.display)