class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        zeros = 0

        for i in range(len(s)):
            if s[i] == '0':
                zeros += 1
            elif s[i] == '1':
                ones += 1
        if ones == 1:
            res = "0"*zeros + "1"
        else:
            ones -= 1
            res = "1"*ones + "0"*zeros + "1"
        
        return res