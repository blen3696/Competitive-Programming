class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)] 
        rank = [0] * (n + 1) 

        def find(u):
            
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return False  
           
            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []
