class DSU:
    def __init__(self, n):
        self.rank = [1] *n 
        self.p = [i for i in range(n)]

    def find(self, node):
        cur = node
        while cur != self.p[cur]:
           # self.p[cur] = self.p[self.p[cur]]
            cur = self.p[cur]
        return cur

    def union(self,u,v):
        p1,p2 = self.find(u), self.find(v)
        
        if p1 == p2:
            return False
        if self.rank[p2] > self.rank[p1]:
            p1,p2 = p2,p1
        self.p[p2] = p1
        self.rank[p2] += self.rank[p1]
        return True






class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res
        