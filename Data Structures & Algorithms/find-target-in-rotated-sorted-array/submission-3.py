class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None:
            return -1
        first = 0
        last = len(nums) - 1
        mid = (last + first) // 2
        
        while first <= last:

            mid = (first + last) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[first]:
                if target >= nums[first] and target <= nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

            else:
                if target > nums[mid] and target <= nums[last]:
                    first = mid + 1
                else:
                    last = mid - 1
        
        return -1