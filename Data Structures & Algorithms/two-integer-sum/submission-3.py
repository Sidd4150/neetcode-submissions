class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = defaultdict(int)

        
        for i, n in enumerate(nums):

            diff = target - n

            if diff in m:
                return [m[diff], i]
            else:
                m[n] = i

        return [] 

        
