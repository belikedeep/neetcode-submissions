class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newS = ""
        maxLen = 0

        for c in s:
            while c in newS:
                newS = newS[1:]

            newS += c
            maxLen = max(maxLen, len(newS))

        return maxLen
            