class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for u,v in edges:

            if not dsu.join(u,v):
                return [u,v]

class DSU:
    def __init__(self,size):
        self.parent = list(range(size+1))

    def find(self, i):

        if self.parent[i] == i :
            return i

        return self.find(self.parent[i])
    
    def join(self, i, j):
        
        rooti = self.find(i)
        rootj = self.find(j)

        if rooti != rootj:
            self.parent[rooti] = rootj
            return True
        return False
