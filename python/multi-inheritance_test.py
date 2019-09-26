class a:
    def __init__(self):
        print("class a inited")
        super().__init__()

class b:
    def __init__(self):
        print("class b inited")
        pass

class c(a,b):
    pass

def init(self):
    print("class object inited")

print(c.__mro__)
c()
