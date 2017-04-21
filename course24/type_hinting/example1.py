# -*- coding: utf-8 -*-

from typing import List

__author__ = 'sobolevn'


class SomeData(object):
    def __init__(self, values: List[str]) -> None:
        self.data = values

    def get_item(self, index: int) -> str:
        return self.data[index]


def print_all(obj: SomeData) -> None:
    for item in obj.data:
        print(item)


s = SomeData(['str2', 'text', '123'])
print_all(s)
