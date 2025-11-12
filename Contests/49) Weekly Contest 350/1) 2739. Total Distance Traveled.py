"""
https://leetcode.com/problems/total-distance-traveled
"""


def distance_traveled(t1: int, t2: int) -> int:
    """"""

    # -1) [WA] Optimal (Calc. directly using maths): TC = O(1); SC = O(1)
    # Calculating kms we'd get from both one by one separately.
    # WA: Input: t1 = 9, t2 = 2

    """
    a = t1 * 10
    b = min((t1//5), t2) * 10

    return a + b
    """

    # Or (pull out `*10` and do in the end):

    """
    a = t1
    b = min(t1//5, t2)

    return (a+b) * 10
    """

    # 1) Sub-optimal (Simulate using loop): TC = O(n//5) ~= O(n); SC = O(1)
    
    """
    a = 0
    
    while t1 >= 5:
        a += 50
        t1 -= 5
        if t2:
            t1 += 1
            t2 -= 1

    return a + (t1*10)
    """

    # Or (pull out `*10` and do in the end):

    a = 0
    
    while t1 >= 5:
        a += 5
        t1 -= 5
        if t2:
            t1 += 1
            t2 -= 1

    return (a+t1) * 10

    # 2) Optimal (Calc. directly using maths): TC = O(1); SC = O(1)
    # https://leetcode.com/problems/total-distance-traveled/solutions/3650469/javacpython-math-o1-by-lee215-1daz
    # https://leetcode.com/problems/total-distance-traveled/solutions/3651083/python-3-1-line-w-explanation-ts-80-92-b-rp8t
