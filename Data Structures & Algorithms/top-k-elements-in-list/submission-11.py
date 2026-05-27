class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        heap = []
        for num , freq in counts.items():
            heapq.heappush_max(heap, (freq,num))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop_max(heap)[1])
        return ans

