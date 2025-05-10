class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = {}

        def dfs(node, c):
            if node in color:
                return color[node] == c
            color[node] = c
            for neighbor in graph[node]:
                if not dfs(neighbor, 1 - c):
                    return False
            return True

        for node in range(n):
            if node not in color:
                if not dfs(node, 0):
                    return False
        return True
