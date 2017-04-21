# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


def normal_function():
    return 4


def generator_function():
    yield 4


async def coroutine_function():
    return 4


print(type(normal_function), type(generator_function), type(coroutine_function))

value = normal_function()
print(value)

value = generator_function()
print(value, next(value))

value = coroutine_function()
print(value)
