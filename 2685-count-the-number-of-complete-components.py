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
        # Create adjacency list representation of the graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize visited array
        visited = [False] * n

        # Initialize count of complete components
        count = 0

        # Iterate over all vertices in the graph
        for i in range(n):
            if not visited[i]:
                # Perform DFS from current vertex to find connected component
                component = set()
                self.dfs(graph, i, visited, component)

                # Check if component is complete
                if self.isComplete(component, graph):
                    count += 1

        return count

    def dfs(self, graph, vertex, visited, component):
        # Mark current vertex as visited
        visited[vertex] = True
        component.add(vertex)

        # Iterate over all neighbors of current vertex
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                self.dfs(graph, neighbor, visited, component)

    def isComplete(self, component, graph):
        # Calculate number of possible edges in a complete graph with the same number of vertices
        numVertices = len(component)
        numPossibleEdges = numVertices * (numVertices - 1) // 2

        # Calculate number of edges in the component
        numEdges = 0
        for vertex in component:
            for neighbor in graph[vertex]:
                if neighbor in component:
                    numEdges += 1

        # Check if number of edges is equal to number of possible edges
        return numEdges // 2 == numPossibleEdges