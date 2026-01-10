# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root]) 

        ans = []

        while queue:
            l_len = len(queue)
            l_sum = 0

            for _ in range(l_len):
                 node = queue.popleft()
                 l_sum += node.val

                 if node.left: queue.append(node.left)
                 if node.right: queue.append(node.right)

            ans.append(l_sum/l_len)

        
        return ans