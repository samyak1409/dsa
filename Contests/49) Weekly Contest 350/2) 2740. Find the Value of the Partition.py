"""
https://leetcode.com/problems/find-the-value-of-the-partition
"""


def find_value_of_partition(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Sort): TC = O(n*log(n)); SC = O(n)
    # Intuition:
    # - We need to minimize the gap/diff between max(arr1) and min(arr2).
    # - So, we only need to care about the max(arr1) and min(arr2),
    # all the other elements in either of the arr doesn't matter.
    # - So, we can just sort, and find the min diff b/w any two corresponding nums (say `a`, `b`).
    # (All the nums in left of `a` goes in arr1, all the nums in right of `b` goes in arr2.)

    nums = sorted(nums)

    # min_diff = float('inf')
    # for i in range(len(nums)-1):
    #     min_diff = min(min_diff, nums[i+1]-nums[i])
    # return min_diff
    
    # Or just:
    return min(nums[i+1]-nums[i] for i in range(len(nums)-1))
