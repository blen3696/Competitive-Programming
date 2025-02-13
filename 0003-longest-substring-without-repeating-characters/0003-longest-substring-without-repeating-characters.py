class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
         mpp = [-1] * 256
   
         l =0
         r = 0
         max_len = 0
    
         while r < len(s) :
             if mpp[ord(s[r])] != -1:
                 if mpp[ord(s[r])] >= l:
                      l = mpp[ord(s[r])] +1
             length = r-l +1
             max_len = max(length,max_len)
             mpp[ord(s[r])] = r
             r +=1
         return max_len
        