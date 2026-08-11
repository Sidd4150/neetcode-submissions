class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        v = set()
        for n in nums:
            if n in v:
                return n
            v.add(n)

        return -1