class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr =[]
        
        pri = [0]*len(s)

        for i in range(len(shifts)):
            if shifts[i][2] == 1:
                
                pri[shifts[i][0]] += 1
                if shifts[i][1] + 1 < len(pri):
                    pri[shifts[i][1] + 1] -= 1
                

            if shifts[i][2] == 0:
                pri[shifts[i][0]] -= 1
                if shifts[i][1] + 1 < len(pri):
                    pri[shifts[i][1] + 1] += 1

        
        for i in range(1,len(pri)):
            pri[i] += pri[i - 1]

 
        for i in range(len(s)):
            char = (ord(s[i]) - ord('a') + pri[i])% 26
            res = chr(char + ord('a'))
            arr.append(res)
          


       

        return "".join(arr)

            
        