# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs):


    dct = {}

    for s in strs:

        val = [0] * 26

        for c in s:
            val[ord(c) - 97] += 1
        
        dct[tuple(val)] = [s] + dct.get(tuple(val), [])
    
    return list(dct.values())






print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))