# https://leetcode.com/problems/permutation-in-string/


def checkInclusion(s1, s2):

    '''O(26n) space'''
    # if len(s2) < len(s1): return False

    # dct1, dct2 = {}, {}

    # for char in s1:
    #     dct1[char] = 1 + dct1.get(char, 0)

    # for i in range(len(s1)):
    #     dct2[s2[i]] = 1 + dct2.get(s2[i], 0)
    
    # if dct1 == dct2: return True

    # l, r = 0, len(s1)

    # for idx in range(r, len(s2)):
    #     dct2[s2[l]] -= 1
    #     if dct2[s2[l]] == 0: del dct2[s2[l]]
    #     l += 1
    #     dct2[s2[idx]] = 1 + dct2.get(s2[idx], 0)

    #     if dct1 == dct2: return True

    # return False



    if len(s2) < len(s1): return False

    dct1, dct2 = {}, {}

    for char in s1:
        dct1[char] = 1 + dct1.get(char, 0)

    matches = 0

    for idx in range(len(s1)):
        dct2[s2[idx]] = 1 + dct2.get(s2[idx], 0)

        if dct2[s2[idx]] == dct1.get(s2[idx]):
            matches += 1

    # print(dct1, dct2)
    # print(matches)
    if matches == len(dct1): return True


    l = 0
    for idx in range(len(s1), len(s2)):
        
        dct2[s2[l]] -= 1
        if s2[l] in dct1 and dct2[s2[l]] < dct1[s2[l]]: matches -= 1 
        if dct2[s2[l]] == 0: del dct2[s2[l]]
        l += 1


        dct2[s2[idx]] = 1 + dct2.get(s2[idx], 0)
        if dct2[s2[idx]] == dct1.get(s2[idx]):
            matches += 1

        # print(dct1, dct2)
        if matches == len(dct1): return True

    return False





print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))
print(checkInclusion("adc", "dcda"))
print(checkInclusion("hello", "ooolleoooleh"))
print(checkInclusion("abcdxabcde", "abcdeabcdx"))