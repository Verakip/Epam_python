"""
Given a cell with "it's a fib sequence" from slideshow,
please write function "check_fib", which accepts a Sequence of integers,
and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence
# import sys
# sys.path.append('C:/Users/Vera_Kipiatkova/Documents/GitHub/Epam_python')
from homework1.task01.code.calc import check_power_of_2


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    Эта функция проверяет, является ли последовательность
    частью последовательности Фибоначчи
    """
    f_2 = data[0]
    a = check_power_of_2(5*f_2**2 + 4)
    if a:
        s = int(a ** 0.5)
    b = check_power_of_2(5*f_2**2 - 4)
    if b:
        s = int(b ** 0.5)
    if a or b:
        t = True
        f_1 = data[1]
        if f_1 != int((f_2 + s)/2):
            t = False
        if t:
            for f in data[2:]:
                if f == f_1 + f_2:
                    f_2, f_1 = f_1, f
                else:
                    t = False
                    break
    else:
        t = False
    return t
