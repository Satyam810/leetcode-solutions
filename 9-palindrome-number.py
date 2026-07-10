    
    # Reverse the input number
    while x != 0:  # Continue until all digits are processed
      lastDigit = x % 10  # Extract the last digit using the modulo operator
      reversedNumber = reversedNumber * 10 + lastDigit  # Append the last digit to the reversed number
      x = x // 10  # Remove the last digit from the original number
    
    reversedNumber = 0  # Initialize the reversed number to 0
    originalNumber = x  # Store the original number
    # Initialize variables to store the original and reversed numbers
    
      return False  # Immediately return false for negative numbers
    if x < 0:  # Negative numbers cannot be palindromes
    # Check if the input number is negative
  def isPalindrome(self, x: int) -> bool:
class Solution:
