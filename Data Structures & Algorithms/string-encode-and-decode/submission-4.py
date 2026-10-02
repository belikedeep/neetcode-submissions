class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for word in strs:
            length = str(len(word))
            encoded_str += length + "#" + word
        
        return encoded_str

    def decode(self, s: str) -> List[str]:

        result = []

        # for i in range(len(s)):
        #     if s[i] is int and s[i] + 1 is "#":
        #         result.append(s[i+2:s[i+1]])

        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            # Extract the word
            word = s[j+1: j+1+length]
            result.append(word)

            # move to the next encoded word
            i = j + 1 + length

        return result