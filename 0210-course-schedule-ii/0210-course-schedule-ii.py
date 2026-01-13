class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0 for _ in range(numCourses)]
        queue = deque()

        res = []

        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()

            res.append(course)

            for nb in graph[course]:
                in_degree[nb] -= 1
                
                if in_degree[nb] == 0:
                    queue.append(nb)

        
        return res if len(res) == numCourses else []

            


