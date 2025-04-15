# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([[root, 0]])
        res = []
        ctn = 0
        curr_arr = []

        while queue:
            node, l = queue.popleft()

            if node != None:
                if ctn != l:
                    res.append(curr_arr[:])
                    curr_arr = []
                    ctn += 1
                curr_arr.append(node.val)
                queue.append([node.left, l + 1])
                queue.append([node.right, l + 1])

        if curr_arr: res.append(curr_arr)

        return res