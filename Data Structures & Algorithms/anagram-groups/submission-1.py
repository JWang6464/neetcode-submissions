class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        maps = {}
        for string in strs:
            character_map = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                character_map[index] += 1
            key = tuple(character_map)
            if key in maps:
                maps[key].append(string)
            else:
                maps[key] = [string]
            
        return list(maps.values())