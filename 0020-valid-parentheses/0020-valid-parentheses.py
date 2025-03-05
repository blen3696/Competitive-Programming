class Solution:
    def isValid(self, s: str) -> bool:
        my_dic = {'(':')','[':']','{':'}'}
        stack = []

        

        for bra in s:
            if bra in my_dic.keys():
                stack.append(bra)
            else:
                if not stack:
                    return False
                clo_bra = stack.pop()

                if my_dic[clo_bra] != bra:
                    return False

        return not stack
                

        