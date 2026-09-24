class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, win = Counter(t), {}
        have = 0
        l = 0
        ans = ""

        for r, c in enumerate(s):
            win[c] = win.get(c, 0) + 1

            if c in need and win[c] == need[c]:
                have += 1

            while have == len(need):
                if not ans or r - l + 1 < len(ans):
                    ans=s[l:r+1]
                
                c=s[l]
                win[c] -= 1

                if c in need and win[c] < need[c]:
                    have -= 1
                l+=1
                
        return ans