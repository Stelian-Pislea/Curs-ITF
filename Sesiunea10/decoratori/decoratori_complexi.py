import functools


def repeat(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat



@repeat(10)
def say_hello(name):
    print(f'Hello {name}')

say_hello('bob')
# say_hello = repeat(10)(say_hello)

# 1. Sa se scrie un context manager care masoara
# durata de executie a unei bucati de cod
from contextlib import contextmanager
from time import perf_counter, sleep


class TimerManager:
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        print(self.end - self.start)


with TimerManager():
    sleep(5)
    print('M-am trezit!')


@contextmanager
def timer_manager():
    start = perf_counter()
    yield
    stop = perf_counter()
    print(stop - start)


with timer_manager() as t:
    sleep(2)
