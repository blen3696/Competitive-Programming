class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ctn = 0
        
        ppl = []
        for i in range(1,n+1):
            ppl.append(i)

        while  len(ppl) > 1:
            ctn =  (ctn + k-1)% len(ppl)
            ppl.remove(ppl[ctn])

            
        return ppl[0] 

            


