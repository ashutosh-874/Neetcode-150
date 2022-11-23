# https://leetcode.com/problems/longest-repeating-character-replacement/


def characterReplacement(s, k):


    dct = {}
    res = 0

    l, r = 0, 0

    while r < len(s):

        dct[s[r]] = 1 + dct.get(s[r], 0)

        most_freq_val = max(dct.values())
        while (r-l+1) - most_freq_val > k:
            dct[s[l]] -= 1
            if dct[s[l]] == 0: del dct[s[l]]
            # most_freq_val = max(dct.values())
            l += 1

        res = max(res, r-l+1)
        print(res)        
        r += 1

    return res


print(characterReplacement("ABABBA", 2))







