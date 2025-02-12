class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = 0
        r = 0
        holder = 0
        res = []

        while r < len(s):
            holder = max(holder,s.rfind(s[r]))
            if holder == r:
                res.append(r - l + 1)
                
                l = r + 1
                
            r += 1

        return res



        