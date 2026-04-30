# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        self.inorder(root, list)
        return list

    
    def inorder(self, root: Optional[TreeNode], list:List[int]):
        if not root:
            return
        self.inorder(root.left,list)
        list.append(root.val)
        self.inorder(root.right,list)

        