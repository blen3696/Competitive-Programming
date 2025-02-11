class Solution:
    def hIndex(self, citations: List[int]) -> int:

        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i

        if len(citations)  == 1:
            if citations[0] != 0:
                return 1
            else:
                return 0
        
        return 0