

class Test(object):
    label = 'Some specific info'

    def __init__(self, number):
        self.number = number

    def method(self):
        print(self.label, self.number)

    @classmethod
    def class_method(cls):
        print(cls.label)

    @staticmethod
    def static_method():
        print('I can not access anything!')


if __name__ == '__main__':
    t = Test(1)
    t.method()
    t.class_method()
    t.static_method()
