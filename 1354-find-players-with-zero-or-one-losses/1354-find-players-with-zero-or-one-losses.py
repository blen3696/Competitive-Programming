class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners_dic = defaultdict(int)
        losers_dic = defaultdict(int)
        win = []
        lose = []
        for num in matches:
            winners_dic[num[0]] +=1
            losers_dic[num[1]] +=1
        for key, value in winners_dic.items():
            if key not in losers_dic:
                win.append(key)
        for key,value in losers_dic.items():
            if value == 1:
                lose.append(key)
        win.sort()
        lose.sort()
        return [win, lose]
