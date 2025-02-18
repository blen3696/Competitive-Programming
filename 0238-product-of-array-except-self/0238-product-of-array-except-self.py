class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =[]
        pre = [1]
        for i in range(len(nums)):
            product = nums[i] * pre[ -1]
            pre.append(product)
     

        post = [1]

        for i in range(len(nums) -1 ,-1,-1):
            pro = nums[i] * post[-1]
            post.append(pro)

        l = 1
        r = len(post) - 2

        while l < len(pre)  and r >= 0:
            res.append(pre[l - 1] * post[r])
            l += 1
            r -= 1
        return res
       
        
        