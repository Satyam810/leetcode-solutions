  # Create an empty stack to store the opening brackets
  stack = []
  
  # Iterate through the input string
  for char in s:
    # If we encounter an opening bracket, push it onto the stack
    if char in bracket_map.values():
      stack.append(char)
    # If we encounter a closing bracket, check if the stack is empty or if the top of the stack does not match the closing bracket
    elif char in bracket_map.keys():
      if not stack or stack.pop() != bracket_map[char]:
        return False
  
  bracket_map = {')': '(', '}': '{', ']': '['}
  # Create a dictionary to map closing brackets to their corresponding opening brackets
def isValid(s):
