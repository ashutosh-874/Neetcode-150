# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s):

    string = ''
    for char in s:
        if char.isalnum():
            string += char.lower()
    
    # print(string)
    return string == string[::-1]


print(isPalindrome('A man, a plan, a canal: Panama'))
print(isPalindrome('race a car'))