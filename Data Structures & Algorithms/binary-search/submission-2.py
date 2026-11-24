class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        if target < nums[0] or target > nums[len_nums-1]:
            return -1
        left, right = 0, len_nums
        while left <= right:
            mid = left + ((right - left)//2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1