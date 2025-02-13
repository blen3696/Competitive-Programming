class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        my_counter1 = Counter(p)
        my_counter2 = Counter(s[:k])
        res = []

        if my_counter1 == my_counter2:
            res.append(0)

        l = 0
        for r in range(k,len(s)):
            my_counter2[s[r]] = my_counter2.get(s[r],0) + 1
            my_counter2[s[l]] = my_counter2.get(s[l],0) - 1
            
            if my_counter2[s[l]] == 0:
                del my_counter2[s[l]]
            l += 1

            if my_counter1 == my_counter2:
                res.append(l)

        return res


            
