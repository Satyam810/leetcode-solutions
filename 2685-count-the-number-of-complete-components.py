"""
You are given an integer n . There is an undirected graph with n vertices, numbered from 0 to n - 1 . You are given a 2D integer array edges where edges[i] = [a i , b i ] denotes that there exists an undirected edge connecting vertices a i and b i . Return the number of complete connected components of the graph . A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph. A connected component is said to be complete if there exists an edge between every pair of its vertices. &nbsp; Example 1: Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]] Output: 3 Explanation: From the picture above, one can see that all of the components of this graph are complete. Example 2: Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]] Output: 1 Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1. &nbsp; Constraints: 1 &lt;= n &lt;= 50 0 &lt;= edges.length &lt;= n * (n - 1) / 2 edges[i].length == 2 0 &lt;= a i , b i &lt;= n - 1 a i != b i There are no repeated edges.
"""

class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Create adjacency list
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        # Find connected components
        visited = [False] * n
        components = []
        for i in range(n):
            if not visited[i]:
                component = []
                self.dfs(i, adjList, visited, component)
                components.append(component)

        # Count complete components
        count = 0
        for component in components:
            if self.isComplete(component, adjList):
                count += 1

        return count

    def dfs(self, vertex, adjList, visited, component):
        visited[vertex] = True
        component.append(vertex)
        for neighbor in adjList[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, adjList, visited, component)

    def isComplete(self, component, adjList):
        n = len(component)
        edges = 0
        for vertex in component:
            for neighbor in adjList[vertex]:
                if neighbor in component:
                    edges += 1
        return edges == n * (n - 1)