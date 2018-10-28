"""
https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
1, 1, 2, 3, 5, 8, 13, …
"""


def recursive_fib(n, memo={}):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        a = memo.get(n - 1, recursive_fib(n - 1))
        b = memo.get(n - 2, recursive_fib(n - 2))
        return a + b


"""
i prevs fib |
0 0, 0  1
1 0, 1  1
2 1, 1  2
3 1, 2  3

"""


def iterative_fib(n):
    prevs = [0, 0]

    for i in range(n):
        if i == 0:
            fib = 1
            prevs = [0, 1]
        else:
            fib = sum(prevs)
            prevs = [prevs[-1], fib]

    return sum(prevs)


n = 9

print(recursive_fib(n))
print(iterative_fib(n))
