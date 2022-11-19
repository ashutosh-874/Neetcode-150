# https://leetcode.com/problems/longest-repeating-character-replacement/


def characterReplacement(s, k):


    dct = {}


    l = 0

    res = 0
    for idx in range(len(s)):

        dct[s[idx]] = 1 + dct.get(s[idx], 0)

        while len(dct) > 2:
            dct[s[l]] -= 1
            if dct[s[l]] == 0: del dct[s[l]]
            l += 1

        if len(dct) < 2:
            res = max(res, idx - l + 1)
            
        k in dct.values():






