"""
https://leetcode.com/problems/neither-minimum-nor-maximum
"""


def find_non_min_or_max(nums: list[int]) -> int:
    """"""

    # 1) Sub-optimal (Sort): TC = O(n*log(n)); SC = O(n)

    if len(nums) < 3:
        return -1

    return sorted(nums)[1]

    # 2) Optimal (Loop and find the min & max first, then find any other num): TC = O(n); SC = O(1)

    # 2.1) Actually, we can just check first 3 nums, we don't even need to traverse whole array.
    # Hence: TC = O(1); SC = O(1)

    # But, `1)` is the best solution to write in the contest, because:
    # - `n` is very small
    # - In contests, write the solution which takes least amount of time to write,
    # which passes the time-space constraints, even if it's not optimal, it doesn't matter while contest.
