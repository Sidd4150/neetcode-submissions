class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        vis = set()
        connected = 0
        for a , b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(curr):

            if curr in vis:
                return 
            vis.add(curr)

            for nei in adj[curr]:
                dfs(nei)

    
        for node in range(n):

            if node not in vis:
                dfs(node)
                connected += 1

        return connected