class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """def rev_inv(s):
            for i in s:
                if i == '0': i = '1'
                elif i == '1': i = '0'

            s = s[::-1]
        
        s = '0'
        for _ in range(n):
            curr_s  = s + "1" + rev_inv(s)
            s = curr_s

        return s[k - 1]"""
        def helper(n):
            if n == 1:
                return ["0"]
            ans =  helper(n-1)
            stack = ['1']
            for i in range(len(ans)-1,-1,-1):
                if ans[i] == '1':
                    stack.append('0')
                else:
                    stack.append('1')
            ans =ans + stack
            return ans
        return helper(n)[k-1]


            
                