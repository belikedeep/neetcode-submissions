class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq.items():
            bucket[freq].append(num)

        result = []

        for num in range(len(bucket) -1,0,-1):
            for i in bucket[num]:
                result.append(i)

                if len(result) == k:
                    return result