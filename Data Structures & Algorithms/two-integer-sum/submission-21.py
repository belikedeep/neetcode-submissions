class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = {}

        for i in range(len(nums)):
            difference = target - nums[i]
        
            if difference in count:
                return [count[difference], i]
        
            count[nums[i]] = i

        return []