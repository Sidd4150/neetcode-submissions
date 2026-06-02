# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []

        Q = []  
        Q.append(root)
        ans.append(root.val)
        while Q:
            
            l = len(Q)
            lvlCheck = False
            
            for _ in range(l):

                curr = Q.pop(0)

                if curr.right and not lvlCheck:
                    ans.append(curr.right.val)
                    lvlCheck = True
                elif curr.left and not lvlCheck:
                    ans.append(curr.left.val)
                    lvlCheck = True

                if curr.right:
                    Q.append(curr.right)
                if curr.left:
                    Q.append(curr.left)
        return ans




