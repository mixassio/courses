#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
import sys

from my_module import my_function


def test_my_module():
    result = my_function(1)
    assert result == False


def wrap(func):
    try:
        func()
    except AssertionError:
        return False
    else:
        return True


def run():
    members = inspect.getmembers(sys.modules[__name__])
    test_functions = [obj for name, obj in members
                     if (inspect.isfunction(obj) and name.startswith('test'))]
    return all(wrap(f) for f in test_functions)


if __name__ == '__main__':
    result = run()
    if result:
        print('Passed')
    else:
        print('Failed')
