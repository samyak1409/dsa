"""
https://leetcode.com/problems/construct-the-longest-new-string
"""


def longestString(x: int, y: int, z: int) -> int:
    """"""

    # Intuition:
    # - Not allowed:
    #   - AAA = xx, xz
    #   - BBB = yy, zy
    # - So, only allowed sequences:
    #   - x -> y
    #   - y -> x, z
    #   - z -> x, z

    # 1) Sub-optimal (Recursion/DFS + Memo: Try all sequences): TC = O(x*y*z*2) = O(x*y*z); SC = O(x*y*z + x+y+z) = O(x*y*z)

    """
    from functools import cache

    @cache
    def r(x: int, y: int, z: int, is_x:bool = False) -> int:
        if is_x:
            # If y is no more available:
            if y == 0:
                # Then we need to stop now:
                return 1
            # Else:
            return r(x, y-1, z) + 1
        # If the current is y/z, next options are the same, viz, x, z. So:
        else:
            # Init with the stop return value, which is 1:
            a = 1
            # If x is available, continue with the process:
            if x != 0:
                a = r(x-1, y, z, True) + 1
            # Init with the stop return value, which is 1:
            b = 1
            # If z is available, continue with the process:
            if z != 0:
                b = r(x, y, z-1) + 1
            # Return max:
            return max(a, b)

    # At first, try starting with all three x, y, z:
    return max(r(x-1, y, z, True), r(x, y-1, z), r(x, y, z-1)) * 2
    """

    # 1) Optimal (Greedy + Maths): TC = O(1); SC = O(1)
    # ChatGPT (5.1):
    # - Alternate AA and BB → `2 * min(x,y)` blocks
    # - Add 1 extra block if one side is larger
    # - If ending block is not AA → append all AB blocks
    # - Return `blocks * 2`
    # Gemini (2.5 Pro):
    # The logic is:
    # 1. You can **always use all `z` ("AB") items** because they can chain with themselves (`z -> z`)
    # or be inserted after `y` ("BB") items.
    # 2. The `x` ("AA") and `y` ("BB") items must form an alternating chain.
    # 3. This chain will have `2 * min(x, y)` items, plus one extra if `x != y`.
    # 4. The final length is `(z + 2 * min(x, y) + (1 if x != y else 0)) * 2`.

    return (z + (2 * min(x, y)) + (x != y)) * 2
