import pytest
import sys
sys.path.append('C:/Users/Vera_Kipiatkova/Documents/GitHub/Epam_python')
from homework1.task01.code.calc import check_power_of_2
#from  calculator.calc import check_power_of_2

@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (65536, True),
        (12, False),
        (128, False),
        (9, True),
        (0, True),
        (-1, False),
        ('spam', False),
        (3.14, False)
    ],
)

def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result

