# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        nodes = []
        if not root:
            return result
        nodes.append(root)
        while len(nodes) > 0:
            level = []
            length = len(nodes)
            for i in range(length):
                level.append(nodes[i].val)
                if nodes[i].left:
                    nodes.append(nodes[i].left)
                if nodes[i].right:
                    nodes.append(nodes[i].right)
            nodes = nodes[length:]
            result.append(level)
        
        return result
        