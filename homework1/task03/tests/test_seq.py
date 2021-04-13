import pytest
from homework1.task03.code.seq import find_maximum_and_minimum
# import sys
# sys.path.append('C:/Users/Vera_Kipiatkova/Documents/GitHub/Epam_python')


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ('homework1/task03/code/seq.txt', (1, 7))
    ],
)
def test_maximum_and_minimum(value: str, expected_result: bool):
    actual_result = find_maximum_and_minimum(value)
    assert actual_result == expected_result
