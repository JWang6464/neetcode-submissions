class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for character in s:
            if character in pairs:
                if not stack or stack[-1] != pairs[character]:
                    return False
                stack.pop()
            else:
                stack.append(character)
            
        return not stack