class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for num in range(len(arr),1,-1):
            i = arr.index(num)
            res.extend([i + 1,num])
            arr = arr[:i:-1] + arr[:i]

        return res




        