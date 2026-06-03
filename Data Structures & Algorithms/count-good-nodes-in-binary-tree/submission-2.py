# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
       
        self.gg = 0
        def dfs(curr, currMax):
            
            if currMax <= curr.val:
                self.gg += 1
            currMax = max(currMax, curr.val)


            if curr.left:
                dfs(curr.left,currMax)
            if curr.right:
                dfs(curr.right,currMax)
  

        dfs(root,root.val)
        return self.gg

            