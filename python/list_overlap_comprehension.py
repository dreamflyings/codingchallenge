"""
https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

... and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your program
works on two lists of different sizes. Write this in one line of Python using
at least one list comprehension.

"""

def list_overlap(a, b):
    return list(set(map(lambda x:x[0] ,zip(sorted(a), sorted(b)))))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

ans = list_overlap(a, b)

print(ans)

