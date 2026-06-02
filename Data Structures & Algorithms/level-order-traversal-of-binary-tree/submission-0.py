# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = []
        Q.append(root)
        levels = []
        while Q:
            l = len(Q)
            lvl = []
            for _ in range(l):
                curr = Q.pop(0)
                lvl.append(curr.val)

                if curr.left:
                    Q.append(curr.left)
                if curr.right:
                    Q.append(curr.right)
            levels.append(lvl)

        return levels