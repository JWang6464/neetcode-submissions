class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = []
        front = 0
        result = []

        for i in range(len(nums)):
            while front < len(deque) and deque[front] <= i - k:
                front += 1

            while len(deque) > front and nums[deque[-1]] < nums[i]:
                deque.pop()

            deque.append(i)

            if i >= k - 1:
                result.append(nums[deque[front]])

            if front > 100:
                deque = deque[front:]
                front = 0

        return result