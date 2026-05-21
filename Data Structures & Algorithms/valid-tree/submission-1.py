class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        m = defaultdict(list)
        vis = set()

        for u,v in edges:
            m[u].append(v)
            m[v].append(u)


        def dfs(curr, parent ):
            
            if curr in vis:
                return False
            
            vis.add(curr)

            for child in m[curr]:
                #loop throguh children 
                if child == parent:
                    continue
                if not dfs(child,curr):
                    return False
            return True


        if not dfs(0,-1):
            return False
        return len(vis) == n