class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for t in s:
            if t.isalnum():
                newStr += t.lower()
        
        return newStr == newStr[::-1]
        