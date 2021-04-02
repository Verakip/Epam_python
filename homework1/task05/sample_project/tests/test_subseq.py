import pytest

from code.subseq import find_maximal_subarray_sum
#from homework1.task01.sample_project.calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (([1, 3, -1, -3, 5, 3, 6, 7], 3), 16)
    ],
)

def test_maximal_subarray_sum(value: tuple, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result

