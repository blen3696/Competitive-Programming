class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = sum(skill)//(len(skill)//2)

        skill.sort()
        l = 0
        r = len(skill) - 1
        chem = 0
        while l < r:
            my_sum = skill[l] + skill[r]
            if my_sum == n:
                chem += skill[l] * skill[r]
                l += 1
                r -=1
            else:
                return -1

        return chem
        