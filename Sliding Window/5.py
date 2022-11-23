# https://leetcode.com/problems/minimum-window-substring/


def minWindow(s, t):

    if len(t) > len(s):
        return ""

    need_dct = {}
    for i in t:
        need_dct[i] = need_dct.get(i, 0) + 1

    need = len(need_dct)


    res, resLength = "", float('inf')

    have, have_dct = 0, {}
    l = 0
    for r in range(len(s)):
        char = s[r]
        
        if char in need_dct:
            have_dct[char] = have_dct.get(char, 0) + 1
            if have_dct[char] == need_dct[char]:
                have += 1
        
        while have == need:

            if (r-l+1) < resLength:
                res = s[l:r+1]
                resLength = r-l+1

            l_char = s[l]
            if l_char in have_dct:
                have_dct[l_char] -= 1
                if have_dct[l_char] < need_dct[l_char]:
                    have -= 1
            l += 1
    
    return res


print(minWindow("cabwefgewcwaefgcf","cae"))
        
        
