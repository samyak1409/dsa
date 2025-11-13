"""
https://leetcode.com/problems/find-maximum-number-of-string-pairs
"""


def maximum_number_of_string_pairs(words: list[str]) -> int:
    """"""

    # 0) Brute (Nested Loop): TC = O(n^2); SC = O(1)
    # For each element one by one, check all the elements in the right.

    """
    cnt = 0
    for i in range(n:=len(words)):
        for j in range(i+1, n):
            if words[i] == words[j][::-1]:
                cnt += 1
    return cnt
    """
 
    # 1) Optimal (HashSet): TC = O(n); SC = O(n)

    hs = set(words)  # for O(1) lookup

    cnt = 0

    for w in words:
        # Edge case:
        if w == w[::-1]:
            # Then, the reverse word matching is the word itself, since strs are distinct.
            # So, skip:
            continue
        # Check reverse:
        if w[::-1] in hs:
            # Just need to remove the current word:
            hs.remove(w)
            cnt += 1
    
    return cnt
