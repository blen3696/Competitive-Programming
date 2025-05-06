class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
     
        n = len(bombs)
        graph = [[] for _ in range(n)]

        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                dx, dy = x1 - x2, y1 - y2
                if dx * dx + dy * dy <= r1 * r1:
                    graph[i].append(j)

        def bfs(start):
            visited = set()
            queue = deque([start])
            visited.add(start)

            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return len(visited)

        return max(bfs(i) for i in range(n))
