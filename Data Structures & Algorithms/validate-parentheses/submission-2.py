class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:

            if c in pairs:

                # No opening brackets available
                # or top opening bracket doesn't match
                if not stack or stack.pop() != pairs[c]:
                    return False
                
            else:
                stack.append(c)

        return not stack