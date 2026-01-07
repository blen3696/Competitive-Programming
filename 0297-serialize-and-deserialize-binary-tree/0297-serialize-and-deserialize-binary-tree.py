# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        
        queue = deque([root])
        res = []

        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: 
                res.append("null")

        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None

        res = data.split(",")
        root = TreeNode(res[0])
        queue = deque([root])

        idx = 1

        while queue:
            node = queue.popleft()

            if res[idx] != "null":
                node.left = TreeNode(res[idx])
                queue.append(node.left)
            
            idx += 1

            if res[idx] != "null":
                node.right = TreeNode(res[idx])
                queue.append(node.right)

            idx += 1

        return root 
            


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))