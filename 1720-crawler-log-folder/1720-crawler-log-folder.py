class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if log == './':
                pass
            elif log =='../':
                if stack:
                    stack.pop()

            else:
                stack.append(log)

        return len(stack)