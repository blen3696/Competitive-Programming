class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        # 0 == red and 1 == blue

        graph = [[] for _ in range(n)]

        for i, j in redEdges:
            graph[i].append((j, 0))
        for i, j in blueEdges:
            graph[i].append((j, 1))

        res = [-1]*n




        queue = deque([(0, 0), (0, 1)])
        visited = set([(0,1),(0,0)])

        level = 0
        while queue:
            for _ in range(len(queue)):
                adj, color = queue.popleft()
                if res[adj] == -1 or res[adj] > level:
                    res[adj] = level

                for nb, col in graph[adj]:
                    if (nb,col) not in visited and col != color:
                        queue.append((nb, col))
                        visited.add((nb, col))
            level += 1

         

        return res