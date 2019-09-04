# doctest

2 ways

## built in functions

may disturbing

```python
import doctest

def fib(n):
    """
    Calculates the n-th Fibonacci number iteratively  

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10) #正确值为55
    56
    >>> fib(15)
    610
    >>>

    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__": 
    doctest.testmod(verbose=True)
```

## use a new file

```python
# end file name with TXT
The ``fibonacci_doctest`` module
======================

Using ``fib``
-------------------

First import fib fuction

    >>> from fibonacci_doctest import fib

Now use it
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10)  # correct will be 55
    56
    >>> fib(15)
    610
```

```python
import doctest

def fib(n): pass

if __name__ == "__main__":
    doctest.testfile("fibonacci_doctest.txt")
```
