
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.inorder(root, 0) is not False
    
    def inorder(self, root: Optional[TreeNode], height: int):
        if not root:
            return height

        left_height = self.inorder(root.left, height + 1)
        if left_height is False: return False
        
        right_height = self.inorder(root.right, height + 1)
        if right_height is False: return False
        
        if abs(left_height - right_height) > 1:
            return False
        else:
            return max(left_height, right_height)