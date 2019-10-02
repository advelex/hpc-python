import numpy as np


def exercise1():
    print('\nEx1')
    values = [1, 2, 4.2, 5]
    optimized = np.array(values)
    print(type(optimized))
    print(optimized)


def exercise2():
    print('\nEx2')
    numbers = np.arange(-2.0, 2.2, 0.2)
    print(numbers)


def exercise3():
    print('\nEx3')
    full = np.linspace(0.5, 1.5, 11)
    print('all', full)
    print('every second', full[::2])


def exercise4():
    print('\nEx4')
    word = list('hello')
    chars = np.array(word, dtype='c')
    print(chars)
    print(repr(chars))


if __name__ == '__main__':
    exercise1()
    exercise2()
    exercise3()
    exercise4()
