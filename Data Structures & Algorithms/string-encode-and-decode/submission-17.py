class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for i in strs:
            length = str(len(i))

            encoded_str += length + "#" + i
        
        return encoded_str

    5#Hello5#world

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []
        while i < len(s):
            j=i
            
            while s[j] != "#":
                j += 1
                
            length = int(s[i:j])
            word = s[j + 1 : j + 1 +length]

            res.append(word)

            i = j + 1 + length

        return res