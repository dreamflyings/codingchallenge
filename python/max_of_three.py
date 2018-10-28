"""
https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

Implement a function that takes as input three variables, and returns the
largest of the three. Do this without using the Python max() function!

"""


def max_of_n(*x):
    max_val = 0
    for val in x:
        if val > max_val:
            max_val = val
    return max_val


print(max_of_n(1, 2, 3, 4, 0, 2))
