class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # straightforward solution
        len_nums = len(nums)
        product = 1
        result = [0] * len_nums
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product*=num
        
        for i in range(0,len_nums):
            if zero_count > 1:
                return result
            elif zero_count == 1:
                result[i] = 0 if nums[i] != 0 else product
            else:
                result[i] = product//nums[i]
        return result