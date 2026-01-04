"""
https://leetcode.com/problems/split-array-by-prime-indices
"""


def splitArray(self, nums: list[int]) -> int:
    """"""

    # 1) Optimal (Sieve of Eratosthenes): TC = O(n*log(log(n)); SC = O(n)

    from math import isqrt

    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode:
    # TC = O(n*log(log(n)); SC = O(n)
    p = [True] * (n := len(nums))
    p[0] = False
    if n > 1:
        p[1] = False
    for i in range(2, isqrt(n)+1):
        if p[i]:  # if prime
            for j in range(i*i, n, i):
                p[j] = False
    # print(p)

    sum1 = sum2 = 0
    for i, num in enumerate(nums):  # O(n); O(1)
        if p[i]:
            sum1 += num
        else:
            sum2 += num

    return abs(sum1-sum2)
