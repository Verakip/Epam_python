import pytest
# import sys
# sys.path.append('C:/Users/Vera_Kipiatkova/Documents/GitHub/Epam_python')
from homework1.task04.code.sum import check_sum_of_4
# from homework1.task01.sample_project.calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, 0], [0, 1], [1, 0], [0, 1], 1),
        ([1, -1], [-1, 1], [1, -1], [-1, 1], 6)
    ],
)
def test_sum_of_four(a: list, b: list, c: list, d: list, expected_result: int):
    """
    тестирует функцию, выдающую количество четверок, в сумме дающих 0
    """
    actual_result = check_sum_of_4(a, b, c, d)
    assert actual_result == expected_result
