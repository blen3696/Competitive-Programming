class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        my_dic = {}
        ctn = 0

        for i in answers:
            if i in my_dic and my_dic[i] > 0:
                my_dic[i] -= 1
            else:
                ctn += i + 1
                my_dic[i] = i
                    

        return ctn

            
            
        