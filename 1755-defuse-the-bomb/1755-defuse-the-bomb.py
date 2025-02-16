class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        result = [0] * n
        extended = code * 2  
        
        for i in range(n):
            if k > 0:
                result[i] = sum(extended[i + 1 : i + k + 1])
            else:
                result[i] = sum(extended[i + n + k : i + n])
        
        return result