import pytest
import sys
sys.path.append('C:/Users/Vera_Kipiatkova/Documents/GitHub/Epam_python')
from homework1.task03.code.seq import find_maximum_and_minimum



#from homework1.task01.sample_project.calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ('seq.txt', [1,7])
    ],
)

def test_maximum_and_minimum(value: str, expected_result: bool):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result

