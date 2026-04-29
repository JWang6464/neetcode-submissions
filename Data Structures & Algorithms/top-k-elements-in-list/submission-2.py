class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        result = []
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        # use bucket sort
        buckets = [[] for i in range(len(nums) + 1)]
        for num, frequency in count_map.items():
            buckets[frequency].append(num)


        for i in range(len(nums), -1, -1):
            for number in buckets[i]:
                result.append(number)

                if len(result) == k:
                    return result

        return result