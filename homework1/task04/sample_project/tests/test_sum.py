import pytest

from code.seq import check_sum_of_four
#from homework1.task01.sample_project.calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([1,0],[0,1],[1,0],[0,1], 1)
        
    ],
)

def test_sum_of_four(value: tuple, expected_result: bool):
    actual_result = check_sum_of_4(value)

    assert actual_result == expected_result

