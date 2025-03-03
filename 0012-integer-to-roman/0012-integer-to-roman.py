class Solution:
    def intToRoman(self, nums: int) -> str:
   
        res = ""
        my_dic = { 1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
            1: 'I'}

        for val, sign in my_dic.items():
            while nums >= val:
                res += sign
                nums -= val

        

        return res


