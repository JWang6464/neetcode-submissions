class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for char in s1:
            index = ord(char) - ord('a')
            count1[index] += 1
        
        left = 0
        for right in range(len(s2)):

            count2[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 > len(s1):
                count2[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if right - left + 1 == len(s1):
                if count1 == count2:
                    return True
        
        return False