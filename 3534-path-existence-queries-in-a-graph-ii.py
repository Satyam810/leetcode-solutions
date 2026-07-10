from collections import deque, defaultdict

class Solution(object):
    def shortestPath(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= maxDiff:
                    graph[i].append(j)
