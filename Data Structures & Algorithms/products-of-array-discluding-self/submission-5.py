class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod, zero_count = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        
        if zero_count > 1:
            return [0]*len(nums)
        
        arr = [0]*len(nums)

        for i in range(len(nums)):
            if zero_count > 0:
                if nums[i] == 0:
                    arr[i] = prod
                else:
                    arr[i] = 0
            
            else:
                arr[i] = prod // nums[i]
        
        return arr


        