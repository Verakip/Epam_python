import pytest
from homework1.task05.code.subseq import find_maximal_subarray_sum
# import sys
# sys.path.append('C:/Users/Vera_Kipiatkova/Documents/GitHub/Epam_python')


@pytest.mark.parametrize(
    ["value", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16)
    ],
)
def test_maximal_subarray_sum(value: list, k: int, expected_result: int):
    """
    тест-функция для выбора подмассива длины к с максимальной суммой
    """
    actual_result = find_maximal_subarray_sum(value, k)
    assert actual_result == expected_result
