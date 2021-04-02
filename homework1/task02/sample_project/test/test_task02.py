import pytest
from homework1.task02 import check_fibonacci




@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([6,4,6], False),
        ([1,2], True),
        ([8,2,1], True),
        ([9], False),
        ([0], True),
        ([-1], False)
    ],
)

def test_check_fibonacci(value: Sequence, expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result