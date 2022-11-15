# https://leetcode.com/problems/valid-anagram/

def isAnagram(s: str, t: str) -> bool:

    dct = {}

    for char in s:
        dct[char] = 1 + dct.get(char, 0)

    for char in t:
        if dct.get(char):
            dct[char] -= 1
            if dct[char] == 0: del dct[char]
        else:
            return False
    
    return not dct

s = "rat"
t = "car"
print(isAnagram(s, t))