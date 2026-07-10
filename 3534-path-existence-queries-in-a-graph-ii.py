function constructGraph(n, nums, maxDiff):
    graph = empty graph
    for i in range(n:
        for j in range(i+1, n):
            if abs(nums[i] - nums[j]) <= maxDiff:
                add edge between i and j to graph
    return graph

function bfs(graph, source, target):
    queue = new queue with source node
    distance = 0
    visited = empty set
    while queue is not empty:
        node = dequeue from queue
        if node is target:
            return distance
