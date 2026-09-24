class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # need: Cunt how many times each character is REQUIRED
        # Example: t = "AABC" -> {'A': 2, 'B': 1, 'C': 1}
        # win = Count characters inside out current sliding window
        need, win = Counter(t), {}

        # have: how many required characters have been satisfied
        # l: left pointer 
        have = 0
        l = 0

        # Smalles valid window
        ans = ""

        # r: right pointer
        for r, c in enumerate(s):

            # add current charactrer to the window
            win[c] = win.get(c, 0) + 1

            # if character is required and we have exactly the required number one req is satisfied

            # need['A']=2  ->  win['A'] becomes 2  ->  have += 1
            if c in need and win[c] == need[c]:
                have += 1

            # if characters are satisfied, shring the window from left
            while have == len(need):

                # Check if it is smaller than our previous answer
                if not ans or r - l + 1 < len(ans):
                    ans=s[l:r+1]
                
                 # Remove the leftmost character
                c=s[l]
                win[c] -= 1

                # If x was required and removing it means we no longer have enogh of it and the window becomes invalid
                if c in need and win[c] < need[c]:
                    have -= 1
                l+=1


        return ans