"""
Given a cell with "it's a fib sequence" from slideshow,
please write function "check_fib", which accepts a Sequence of integers,
and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence
import sys
sys.path.append('C:/Users/Vera_Kipiatkova/Documents/GitHub/Epam_python')
from homework1.task01.code.calc import check_power_of_2
# from homework1.task01.calculator.calc import check_power_of_2


def check_fibonacci(data: Sequence[int]) -> bool:
    t = True
    for d in data:
        if d < 0:
            return False
        else:
            a = check_power_of_2(5*d**2 + 4)
            b = check_power_of_2(5*d**2 - 4)
            if a or b:
                t = t and True
            else:
                t = t and False
    return t
