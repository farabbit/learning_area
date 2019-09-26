import functools

def display(func):
    @functools.wraps(func)
    def targetFunc(*args):
        result = func(*args)
        print("%s(%s) ---> %s" % (func.__name__, *args, str(result)))
        return result
    return targetFunc

@display
@functools.lru_cache(12)
def fib(n): return 1 if n <= 2 else fib(n-1)+fib(n-2)

def fibGene(n):
    a,b=0,1
    for i in range(n):
        yield b
        a,b=b,a+b
        

fib(10)
print(list(fibGene(10)))
