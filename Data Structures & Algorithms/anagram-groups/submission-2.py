class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            char_map = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                char_map[index] += 1
            key = tuple(char_map)
            if key in groups:
                groups[key].append(string)
            else:
                groups[key] = [string]
        return list(groups.values())