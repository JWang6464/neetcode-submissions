class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l, r = 0, 1
        result = []
        num_days = 1
        while l < len(temperatures):
            if r > len(temperatures) - 1:
                result.append(0)
                l += 1
                r = l + 1
                num_days = 1
            elif temperatures[r] > temperatures[l]:
                result.append(num_days)
                num_days = 1
                l += 1
                r = l + 1
            else:
                num_days += 1
                r += 1
        
        return result