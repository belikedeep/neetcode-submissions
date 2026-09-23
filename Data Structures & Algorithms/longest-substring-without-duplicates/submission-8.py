class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        maxLen = 0
        l = 0

        for x in range(len(s)):
            while s[x] in char:
                char.remove(s[l])
                l += 1
            char.add(s[x])
            maxLen = max(maxLen, x - l + 1)

        return maxLen