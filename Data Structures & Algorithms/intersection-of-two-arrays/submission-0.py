class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = defaultdict(int)
        ans = set()
        if len(nums1) >= len(nums2):
            for k in nums1:
                m[k] = 1
            for n in nums2:
                if m[n] == 1:
                    ans.add(n)
        else:
            for k in nums2:
                m[k] = 1
            for n in nums1:
                if m[n] == 1:
                    ans.add(n)

        return list(ans)
        