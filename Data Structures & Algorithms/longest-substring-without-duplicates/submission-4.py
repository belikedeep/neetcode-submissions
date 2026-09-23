class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newS = ""
        maxLen = 0

        for x in s:
            while x in newS:
                newS = newS[1:]

            newS += x
            maxLen = max(maxLen, len(newS)) 
        
        return maxLen

        