"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l)
there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
from itertools import product


def check_sum_of_4(a: List[int], b: List[int],
                   c: List[int], d: List[int]) -> int:
    """
    Ищет количество четверок в сумме дающих 0
    """
    counter_of_combinations = 0
    # for i in a:
    #     for j in b:
    #         for k in c:
    #             for m in d:
    #                 if i + j + k + m == 0:
    #                     counter_of_combinations += 1

    for elem in product(a, b, c, d):
        if sum(elem) == 0:
            counter_of_combinations += 1
    return counter_of_combinations
