class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Convert to (number, frequency)
        arr = [] 

        for num, count in freq.items():
            arr.append([num, count])

        # Sort by frequency
        arr.sort(key=lambda x:x[1], reverse=True)

        # Take top k
        result = []

        for i in range(k):
            result.append(arr[i][0])

        return result