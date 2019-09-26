import functools

def initMonitor(_type):
    def initWrapper(initFunc):
        @functools.wraps(initFunc)
        def __init(*args, **kwargs):
            functionCall = "%s.__init__(%s%s)" % (_type,
                                                  ", ".join(map(str,args[1:]))+", " if len(args)>1 else "",
                                                  str(kwargs)[1:-1].replace("'", "").replace(": ","="))
            print("enter %s" % functionCall)
            initFunc(*args, **kwargs)
            print("exit %s" % functionCall)
        return __init
    return initWrapper

if __name__ == "__main__":
    class A:
        @initMonitor('A')
        def __init__(self, a, b):
            print("start init A")

    A(1,b=2)
    """
    enter A.__init__(1, b=2)
    start init A
    exit A.__init__(1, b=2)
    """
