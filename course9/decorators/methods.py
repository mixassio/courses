import time

def print_execution_time(func):
    def _inner(*args, **kwargs):
        print('Inner got:', args, kwargs)
        start = time.time()

        result = func(*args, **kwargs)

        print('Execution time:', time.time() - start)
        return result

    print('F is ', func)
    # _inner(1, 2, 3)

    return _inner


@print_execution_time
def long_functon(dd='Value'):
    print('Starting long function', dd)
    time.sleep(3)


class Calculator(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    @print_execution_time  #()
    def do_sum(self):
        return self.first + self.second

    @print_execution_time
    def do_multiply(self):
        return self.first * self.second


if __name__ == '__main__':
    long_functon(dd='Key')

    calc = Calculator(3, 5)
    print(calc.do_sum())
    print(calc.do_multiply())

