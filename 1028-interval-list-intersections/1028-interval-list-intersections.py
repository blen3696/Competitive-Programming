class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
       
        
        l = 0
        r = 0
        res = []

        while l < len(firstList) and r < len(secondList):
            first_l, first_r = firstList[l]
            second_l, second_r = secondList[r]

            if first_l > second_r:
                r += 1
            elif second_l > first_r:
                l += 1
            else:
                res.append([max(first_l,second_l),min(first_r,second_r)])
                if first_r < second_r:
                    l += 1
                else:
                    r += 1
        return res


               