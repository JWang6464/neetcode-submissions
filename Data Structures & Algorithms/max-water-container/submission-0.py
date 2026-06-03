class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftWall = 0
        rightWall = len(heights) - 1
        maxWater = 0
        while leftWall < rightWall:
            width = rightWall - leftWall
            height = min(heights[leftWall], heights[rightWall])
            area = width * height
            maxWater = max(maxWater, area)

            if heights[leftWall] < heights[rightWall]:
                leftWall += 1
            else:
                rightWall -= 1
        
        return maxWater