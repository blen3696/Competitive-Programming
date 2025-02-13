class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        my_set = set()
        l = 0
        r = 0
        max_len = 0
        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            my_set.add(s[r])
            max_len = max(max_len,r - l + 1)

        return max_len
            

        