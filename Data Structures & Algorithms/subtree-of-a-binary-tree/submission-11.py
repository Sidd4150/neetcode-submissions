# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        
        def same_dfs(curr,tmbSub):


            if curr == None and tmbSub == None:
                return True
            if curr and tmbSub and curr.val == tmbSub.val :
                return same_dfs(curr.left, tmbSub.left) and  same_dfs(curr.right, tmbSub.right)
            return False
        


        if not subRoot:
            return True
        if not root:
            return False


        if same_dfs(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))