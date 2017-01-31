# -*- coding: utf-8 -*-


# map

def work(value):
    return x * 2

t = [1, 2, 10]
m = map(t, work)
print(m)

# The same, but using lambda function
m1 = map(t, lambda x: x * 2)
print(m1)


# filter

print(filter([-1, -5, -9, 20, 3, 0], lambda v: v > 0))


# reduce

from functools import reduce

r = [1, 4, 2, 3]

result = reduce(lambda x, y: x + y, r)
print(result)
