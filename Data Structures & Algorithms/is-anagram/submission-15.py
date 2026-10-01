class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False

        s_store = {}
        t_store = {}

        for char in s:
            s_store[char] = s_store.get(char,0) + 1

        for char in t:
            t_store[char] = t_store.get(char,0) + 1

        return s_store == t_store