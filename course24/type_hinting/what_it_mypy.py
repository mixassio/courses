# -*- coding: utf-8 -*-

from typing import Iterator

__author__ = 'sobolevn'


def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


numbers = fib(10)
for n in numbers:
    print(n)
