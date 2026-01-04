"""
https://leetcode.com/problems/process-string-with-special-operations-i
"""


def processStr(self, s: str) -> str:
    """"""

    # 1) Optimal (Simulate: Loop + `list` instead of `str`): TC = O(2^n); SC = O(2^n)
    # (Think why time and space is 2^n.)

    result = []
    for c in s:
        if c.isalpha():
            result.append(c)
        elif c == '*':
            result.pop() if result else None
        elif c == '#':
            result.extend(result)
        elif c == '%':
            result.reverse()
    return ''.join(result)
