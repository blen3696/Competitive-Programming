class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for cha in s:
            if cha == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(cha)

        for cha in t:
            if cha == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(cha)

        if stack_s == stack_t:
            return True
        else:
            return False

