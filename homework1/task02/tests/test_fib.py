import pytest
# sys.path.append('C:/Users/Vera_Kipiatkova/Documents/GitHub/Epam_python')
from homework1.task02.code.fib import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([6, 4, 6], False),
        ([1, 1, 2], True),
        ([8, 2, 1], False)
    ],
)
def test_check_fibonacci(value: list, expected_result: bool):
    """
    Тестирует функцию, проверяющую последовательность на Фибоначчи
    """
    actual_result = check_fibonacci(value)
    assert actual_result == expected_result
