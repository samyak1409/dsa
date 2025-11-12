"""
https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation
"""


def smallest_string(s: str) -> str:
    """"""

    # 1) Optimal (Greedy, Loop): TC = O(n); SC = O(n)
    # Intuition:
    # - Since lexicographically smallest, we just need to focus on making the first-most char smaller.
    # - And then keep making next chars smaller, until we hit `a`, since that would change to `z`,
    # which would actually increase the lexicographic weight.
    # Why stop?
    # - Because we can perform on any one *substring*.

    a = []
    
    modified = stop = False  # flags
    for c in s:
        # We'd not start modifying until we find a char other than `a`:
        if c == 'a':
            # Till then, we'd not modify, just append the unchanged `a`:
            a.append('a')
            # If the modification was in progress, set to stop modification:
            if modified:
                stop = True
        else:
            if not stop:
                # Modify:
                a.append(chr(ord(c)-1))
                modified = True
            else:
                a.append(c)
    
    # E.g. Input: s = "aa", for cases like these:
    if not modified:
        a[-1] = 'z'        
    
    return ''.join(a)
