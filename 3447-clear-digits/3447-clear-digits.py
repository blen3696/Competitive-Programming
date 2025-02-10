class Solution:
    def clearDigits(self, s: str) -> str:
        digit = ["1","2","3","4","5","6","7","8","9","0"]
        stack = []

        for char in s:
            if char in digit:
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return "".join(stack)