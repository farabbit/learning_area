from initMonitor import initMonitor

class A:
    @initMonitor("A")
    def __init__(self,a):
        print("start init A")
        self.a = a # consume a

class B(A):
    @initMonitor("B")
    def __init__(self,a,b,**kwargs):
        super().__init__(a=a, **kwargs)

        print("start init B")
        self.b = b # consume b

class C(A):
    @initMonitor("C")
    def __init__(self,a,c,**kwargs):
        super().__init__(a=a, **kwargs)

        print("start init C")
        self.c = c # consume c

class D(B,C):
    @initMonitor("D")
    def __init__(self,a,b,c,d):
        super().__init__(a=a,b=b,c=c)

        print("start init D")
        self.d = d # consume d

print("__mro__:", D.__mro__)
d_i = D(1,2,c=3,d=4)
print(d_i.a, d_i.b, d_i.c, d_i.d)
"""
__mro__: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
enter D.__init__(1, 2, c=3, d=4)
enter B.__init__(a=1, b=2, c=3)
enter C.__init__(a=1, c=3)
enter A.__init__(a=1)
start init A
exit A.__init__(a=1)
start init C
exit C.__init__(a=1, c=3)
start init B
exit B.__init__(a=1, b=2, c=3)
start init D
exit D.__init__(1, 2, c=3, d=4)
1 2 3 4
"""
