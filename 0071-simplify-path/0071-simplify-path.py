class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        arr = path.split('/')
        print(arr)

        for i in arr:
            if i == "..":
                if stack:
                    stack.pop() 
            elif i == "." or i == "":
                pass
            else:
                stack.append(i)

        return "/" + "/".join(stack)

            