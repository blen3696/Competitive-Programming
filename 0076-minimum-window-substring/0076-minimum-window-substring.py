class Solution:
    def minWindow(self, s: str, t: str) -> str:
        my_dic1 = Counter(t)
        my_dic2 = defaultdict(int)
        n = len(s)
        
        acquired = 0
        required = len(my_dic1)

        l = 0
        sol = (-1,n+1)
        for r in range(len(s)):
            my_dic2[s[r]] +=  1

            if s[r] in my_dic1:
                if my_dic1[s[r]] == my_dic2[s[r]]:
                    acquired += 1

            while acquired == required:
                if sol[1] - sol[0] > r - l:
                    sol = (l,r)

                my_dic2[s[l]] -= 1
                if s[l] in my_dic1:
                    if my_dic2[s[l]] < my_dic1[s[l]]:
                         acquired -= 1
                l += 1
           
        if sol[0] == -1:
            return ""
        else:
            return s[sol[0]:sol[1]+1]
             