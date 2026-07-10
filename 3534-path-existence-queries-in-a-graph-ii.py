class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and abs(nums[i] - nums[j]) <= maxDiff:
                    graph[i].append(j)
        answer = []
        for ui, vi in queries:
            min_distance = float('inf')
            for i in range(n):
                if ui in graph[i] and vi in graph[i]:
                    min_distance = min(min_distance, abs(i - ui) + abs(i - vi))
            answer.append(min_distance if min_distance != float('inf') else -1)
        return answer
