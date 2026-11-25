class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff not in nums_map:
                nums_map[nums[i]] = i
            else:
                return [nums_map[diff],i] 