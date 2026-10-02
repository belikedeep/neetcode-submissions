class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sort = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))

            if key in sort:
                sort[key].append(strs[i]) 

            else:
                sort[key] = []
                sort[key].append(strs[i]) 

        return list(sort.values())