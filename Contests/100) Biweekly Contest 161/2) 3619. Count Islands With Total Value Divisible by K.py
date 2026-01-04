"""
https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k
"""


def countIslands(self, g: list[list[int]], k: int) -> int:
    """"""

    # EASY: Straight-forward DFS

    # 1) Optimal (DFS): TC = O(m*n); SC = O(m*n)

    m, n = len(g), len(g[0])
    v = set()  # track visited cells
    ans = 0

    # DFS function:
    def dfs(i, j):
        # Stop cases:
        # Out of grid / cell is 0 / cell already visited:
        if not (0 <= i < m and 0 <= j < n) or g[i][j] == 0 or (i, j) in v:
            return 0
        # Add to visited:
        v.add((i, j))
        # Sum of current and all neighbor:
        return g[i][j] + dfs(i, j - 1) + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j)

    # DFS from every cell:
    for i in range(m):
        for j in range(n):
            # If cell is not 0 and not visited:
            if g[i][j] and (i, j) not in v:
                if dfs(i, j) % k == 0:
                    ans += 1

    return ans
