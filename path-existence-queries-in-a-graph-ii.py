from collections import deque

class Solution:
    def shortestPath(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[i] - nums[j]) <= maxDiff:
                    graph[i].append(j)
                    graph[j].append(i)

        result = []
        for u, v in queries:
            queue = deque([(u, 0)])
            visited = set([u])
            while queue:
