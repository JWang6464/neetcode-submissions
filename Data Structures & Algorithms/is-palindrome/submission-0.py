class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters = []

        for character in s.lower():
            if character.isalnum():
                characters.append(character)
        
        return characters == characters[::-1]