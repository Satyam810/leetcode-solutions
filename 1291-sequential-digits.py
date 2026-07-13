"""
An&nbsp;integer has sequential digits if and only if each digit in the number is one more than the previous digit. Return a sorted list of all the integers&nbsp;in the range [low, high] &nbsp;inclusive that have sequential digits. &nbsp; Example 1: Input: low = 100, high = 300 Output: [123,234] Example 2: Input: low = 1000, high = 13000 Output: [1234,2345,3456,4567,5678,6789,12345] &nbsp; Constraints: 10 &lt;= low &lt;= high &lt;= 10^9
"""

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(1, 10 - length + 1):
                num = 0
                for i in range(length):
                    num = num * 10 + start + i
                if low <= num <= high:
                    result.append(num)
        return result