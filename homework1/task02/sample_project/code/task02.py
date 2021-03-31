"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence
from homework1.task01.sample_project.calculator.calc import check_power_of_2

def check_fibonacci(data: Sequence[int]) -> bool:
    t = true
    for d in data:
        a = check_power_of_2(5*d**2+4)
        b = check_power_of_2(5*d**2-4)
        if a or b:
            t = t and True
        else:
            t = t and False
    return t
credits



