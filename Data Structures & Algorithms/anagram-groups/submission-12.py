class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = {}

        for i in range(len(strs)):

            key = "".join(sorted(strs[i]))

            if key in count:
                count[key].append(strs[i])
            
            else:
                count[key] = []
                count[key].append(strs[i])
        
        return list(count.values())