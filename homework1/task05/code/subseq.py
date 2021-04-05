"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    N = len(nums)
    Ma=max(nums)
    l = min(k,N)
    for i in range(2,l+1):
        for j in range(N-i+1):
            s=0
            for k in range(i):
                s = s + nums[j + k]
            if s > Ma:
                Ma = s
    return Ma












