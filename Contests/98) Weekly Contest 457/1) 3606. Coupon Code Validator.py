"""
https://leetcode.com/problems/coupon-code-validator
"""


def validateCoupons(cd: list[str], bl: list[str], ac: list[bool]) -> list[str]:
    """"""

    # 1) Optimal (Simulate: Loop, Sort): TC = O(n*m + m*n*log(n)); SC = O(m+n)
    # 1 WA Penalty:
    # Edge case: cd[i] = "_" (cd[i] contains just one or more underscores)

    res = []
    c_set = {"electronics", "grocery", "pharmacy", "restaurant"}

    for c, b, a in zip(cd, bl, ac):  # O(n*m); O(m)
        c_ = c.replace("_", "")
        if c and (c_ == "" or c_.isalnum()) and b in c_set and a:
            res.append((b, c))

    return [c for _, c in sorted(res)]  # O(m*n*log(n)); O(n)
