class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket method

        # get frequencies
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # create a bucket
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq.items():
            bucket[freq].append(num)
        
        # iterate from highest to lowest
        result = []

        for i in range(len(bucket) -1,0,-1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result










