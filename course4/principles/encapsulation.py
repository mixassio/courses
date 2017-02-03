# -*- coding: utf-8 -*-


class Example(object):
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3

        print('{} {} {}'.format(self.a, self._b, self.__c))


if __name__ == '__main__':
    example = Example()

    print(example.a)
    print(example._b)

    try:
        print(example.__c)
    except AttributeError as ex:
        print(ex)
