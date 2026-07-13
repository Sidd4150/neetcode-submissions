class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = defaultdict(list)

        for u,v,w in times:
            edges[u].append((v,w))

        minHeap = [(0,k)]
        vis = set()
        t = 0 
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)

            if n1 in vis:
                continue
            vis.add(n1)
            t = max(t,w1)

            for n2, w2 in edges[n1]:
                if n2 not in vis:
                    heapq.heappush(minHeap,(w1+w2, n2))

        return t if len(vis) == n else -1