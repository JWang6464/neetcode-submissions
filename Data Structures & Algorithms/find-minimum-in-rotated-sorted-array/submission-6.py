class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = 0
        
        if nums is None:
            return 0
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while left < right:
            if nums[left] <= nums[right]:
                return nums[left]
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            mid = (left + right) // 2
                

        return nums[left]