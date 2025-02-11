class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        print(citations)
         
        h_idx = 0

        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
            


        return 0
            
