class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]

        for i, j in prerequisites:
            graph[i].append(j)

        visited = [-1]*numCourses

        def dfs(node):
            if visited[node] == 0:
                return False
            if visited[node] == 1:
                return True
            visited[node] = 0
            for nb in graph[node]:
                if not dfs(nb):
                    return False
            visited[node] = 1


            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True



            
