# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def swapTree(node):
            if node is None:
                return
            node.left,node.right = node.right, node.left
            swapTree(node.left)
            swapTree(node.right)
        swapTree(root)
        return root
        
        
            

            

        