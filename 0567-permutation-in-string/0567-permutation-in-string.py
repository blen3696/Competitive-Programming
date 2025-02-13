class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        k = len(s1)
        my_dic1 = defaultdict()
        my_dic2 = defaultdict()

        for i in range(k):
            my_dic1[s1[i]] = my_dic1.get(s1[i], 0) + 1
            my_dic2[s2[i]] = my_dic2.get(s2[i], 0) + 1

        if my_dic1 == my_dic2:
            return True

        l = 0
        for r in range(k,len(s2)):
            my_dic2[s2[r]] = my_dic2.get(s2[r], 0) + 1
            my_dic2[s2[l]] = my_dic2.get(s2[l], 0) - 1
            if my_dic2[s2[l]] == 0:
                del my_dic2[s2[l]]
            l += 1

            if my_dic1 == my_dic2:
                return True
        
        return False



        