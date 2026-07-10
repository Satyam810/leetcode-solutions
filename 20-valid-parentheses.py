def isValid(s: str) -> bool:
  # Create a dictionary to map closing parentheses to their corresponding opening parentheses
  parentheses_map = {')': '(', '}': '{', ']': '['}
  
  # Create an empty stack to store the opening parentheses
  stack = []
  
  # Iterate through each character in the input string
  for char in s:
    # If the character is an opening parenthesis, push it onto the stack
    if char in parentheses_map.values():
      stack.append(char)
    # If the character is a closing parenthesis
    elif char in parentheses_map.keys():
      # Check if the stack is empty or if the top of the stack does not contain the corresponding opening parenthesis
      if not stack or stack.pop() != parentheses_map[char]:
