# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(string):

    if len(string) <= 1: return len(string)

    hash_set = set()
    hash_set.add(string[0])

    left_idx = 0
    res = 1

    for idx in range(1, len(string)):
        char = string[idx]
        if char in hash_set:
            res = max(res, (idx - left_idx))
            while char in hash_set:
                hash_set.remove(string[left_idx])
                left_idx += 1
            hash_set.add(char)
        else:
            hash_set.add(char)
    
    res = max(res, len(hash_set))
    return res


print(lengthOfLongestSubstring("abcabcbb"))        
print(lengthOfLongestSubstring("bbbb"))        
print(lengthOfLongestSubstring("pwwkew"))        
print(lengthOfLongestSubstring("qu"))        
print(lengthOfLongestSubstring("dvdf"))        



