class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        ans = [None] * len_nums * 2
        for i in range(0,len(ans)):
            if i < len_nums:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i-len_nums]
        return ans
