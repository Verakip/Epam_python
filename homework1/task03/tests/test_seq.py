# import pytest
from homework1.task03.code.seq import find_maximum_and_minimum
# import sys
# sys.path.append('C:/Users/Vera_Kipiatkova/Documents/GitHub/Epam_python')
import os


def test_maximum_and_minimum():
    """
    Тестирует функцию, ищущую максимум и минимум в текстовом файле
    """
    actual_result = find_maximum_and_minimum(os.path.dirname(__file__)
                                             + '/seq.txt')
    assert actual_result == (1, 7)
