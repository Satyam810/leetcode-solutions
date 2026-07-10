Function buildGraph(n, nums, maxDiff):
  Create an empty adjacency list
  For each node i in the adjacency list:
    For each node j in the nums array:
      If abs(nums[i] - nums[j]) <= maxDiff:
        Add node j to the adjacency list of node i
  Return the adjacency list

Function bfs(graph, start, end):
  Create a queue and enqueue the start node
  Create a visited set and add the start node
  While the queue is not empty:
    Dequeue a node
    If the node is the end node:
      Return the distance from the start node to the end node
    For each neighbor of the node:
