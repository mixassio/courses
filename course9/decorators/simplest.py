# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


def decorator(func):
    def _inner(value):
        print(value)
        return func(value)
    return _inner


@decorator  # == _inner = decorator(square)
def square(i):
    return i ** 2


def triple(i):
    return i * 3


if __name__ == '__main__':
    # _inner = decorator(square)
    print(square(3))

    decorated = decorator(triple)
