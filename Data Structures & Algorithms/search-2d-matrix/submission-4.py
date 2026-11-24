class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            lower_bound = matrix[i][0]
            upper_bound = matrix[i][col - 1]
            if target >= lower_bound and target <= upper_bound:
                return self.search_arr(matrix[i],target)
        return False

    def search_arr(self,nums,target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left)//2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return True
        return False