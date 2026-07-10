            for j in range(n):
                if i != j and abs(nums[i] - nums[j]) <= maxDiff:
                    graph[i].append(j)

        answer = []
        for source, destination in queries:
            queue = deque([(source, 0)])
            visited = {source}
            found = False
            while queue:
        graph = [[] for _ in range(n)]
        for i in range(n):
class Solution:
    def shortestPath(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
from collections import deque

