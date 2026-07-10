class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        result = ""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                result += chars[0]
            else:
                break
        return result
