class Solution:
    def isValid(self, s: str) -> bool:

        s_open = ['(','{','[']
        s_close = [')','}',']'] 
        
        stack = []

        for i in range(len(s)):
            if s[i] in s_open:
                stack.append(s[i])
            elif s[i] in s_close:
                if len(stack) == 0:
                    return False

                if s_open[s_close.index(s[i])] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
                
