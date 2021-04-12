"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l)
there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_4(a: List[int], b: List[int],
                   c: List[int], d: List[int]) -> int:
    s = 0
    N = len(a)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for m in range(N):
                    if a[i]+b[j]+c[k]+d[m] == 0:
                        s += 1
    return s
