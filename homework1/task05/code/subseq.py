"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List
from itertools import islice


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    находим максимальную сумму подмассив длины, не превышающей k
    """
    Len_of_list = len(nums)
    Ma = max(nums)
    min_kN = min(k, Len_of_list)
    for k in range(2, min_kN + 1):
        for i in range(Len_of_list-k+1):
            sub_nums = list(islice(nums, i, i + k))
            summa = sum(sub_nums)
            if summa > Ma:
                Ma = summa

    return Ma
