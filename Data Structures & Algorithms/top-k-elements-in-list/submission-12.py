class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        

        min_heap = []

        for num, freq in counts.items():
            
            heapq.heappush(min_heap, (freq,num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        ans = []
        for n in list(min_heap):
            ans.append(n[1])
        return ans