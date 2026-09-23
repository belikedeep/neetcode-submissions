class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        maxLen = 0

        for x in range(len(s)):
            while s[x] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[x])
            maxLen = max(maxLen, x-l+1)
        return maxLen 