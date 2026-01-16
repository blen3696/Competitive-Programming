class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue = deque()
        out_degree = [0 for _ in range(len(graph))]
        out_d_graph = [[] for _ in range(len(graph))]

        for u in range(len(graph)):
            out_degree[u] += len(graph[u])
            for v in graph[u]:
                out_d_graph[v].append(u)

        
                
        for node in range(len(graph)):
            if out_degree[node] == 0: queue.append(node)

        res = [False] * len(graph)

        while queue:
            node = queue.popleft()

            res[node] = True

            for nb in out_d_graph[node]:
                out_degree[nb] -= 1
                if out_degree[nb] == 0:
                    queue.append(nb)

        return [i for i in range(len(res)) if res[i] != False]