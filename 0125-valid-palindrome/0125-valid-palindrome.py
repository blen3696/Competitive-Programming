class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1

        while l <= r:
            if not s[r].isalnum():
                r -= 1
                continue
            elif not s[l].isalnum():
                l += 1
                continue
            if s[r].lower() == s[l].lower():
                l += 1
                r -= 1
            else:
                return False

        return True 


        