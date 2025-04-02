class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        my_dic = Counter(nums)
        res = []

        for key, val in my_dic.items():
            if val == 2:
                res.append(key)

        return res
