class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = [0] * (n + 1)  

        for i, j in trust:
            res[i] -= 1  
            res[j] += 1 

        for i in range(1, n + 1):
            if res[i] == n - 1:
                return i 

        return -1  
