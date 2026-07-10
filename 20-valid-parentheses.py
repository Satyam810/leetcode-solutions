class Solution:
    def isValid(self, s):
        bracket_map = {')': '(', '}': '{', ']': '['}
        opening_brackets = set(['(', '{', '['])
        stack = []
        
        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in bracket_map.keys():
                if not stack or stack.pop() != bracket_map[char]:
                    return False
        
        return not stack
