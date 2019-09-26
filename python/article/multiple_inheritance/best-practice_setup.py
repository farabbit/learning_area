from initMonitor import initMonitor

class A:
    @initMonitor("A")
    def __init__(self):
        print("start init A")

    def setup_A(self,a):
        self.a=a

class B(A):
    @initMonitor("B")
    def __init__(self):
        print("start init B")
        super().__init__()

    def setup_A(self,a):
        self.a=a

class C(A):
    @initMonitor("C")
    def __init__(self):
        print("start init C")
        super().__init__()

class D(B,C):
    @initMonitor("D")
    def __init__(self):
        print("start init D")
        super().__init__()

print("__mro__:", D.__mro__)
d_i = D()
print(d_i.a, d_i.b, d_i.c, d_i.d)
