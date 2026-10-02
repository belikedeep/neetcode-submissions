class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for i in range(len(nums)):

            if nums[i] in freq:
                freq[nums[i]] += 1
            
            else:
                freq[nums[i]] = 1
            
        # sort the hashmap

        sorted_freq = sorted(freq.items(), key=lambda x:x[1] , reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_freq[i][0])

        return result