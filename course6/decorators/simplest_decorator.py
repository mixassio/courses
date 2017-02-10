# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


def log(function):
    def inner(x, y):
        result = function(x, y)
        print('Result is', result)
        return result
    return inner


def sum(x, y):
    return x + y


def mult(x, y):
    return x * y


s = log(sum)
s(9, 12)

m = log(mult)
m(2, 5)

print(s, m)
