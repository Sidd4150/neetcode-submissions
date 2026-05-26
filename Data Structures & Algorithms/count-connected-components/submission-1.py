class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        #adj list
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        vis = set()
        comp = 0

        def dfs(curr):
            
            if curr in vis:
                return 
            
            vis.add(curr)

            for nei in graph[curr]:
                dfs(nei)

        

        for curr in range(n):
            if curr not in vis:
                dfs(curr)
                comp += 1

        return comp