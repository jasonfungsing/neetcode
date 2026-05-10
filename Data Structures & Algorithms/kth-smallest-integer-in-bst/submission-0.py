# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self.inorder(root, k, result)
        return  result[k-1] 
    

    def inorder(self, root: Optional[TreeNode], k: int, result:[int]):
        if not root or len(result)>= k:
            return result   
        self.inorder(root.left, k, result)
        result.append(root.val)
        self.inorder(root.right, k, result)