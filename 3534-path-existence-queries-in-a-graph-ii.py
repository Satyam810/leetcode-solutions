class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        for i in range(n):
            graph[i] = []
            for j in range(n):
                if i != j and abs(nums[i] - nums[j]) <= maxDiff:
                    graph[i].append(j)

