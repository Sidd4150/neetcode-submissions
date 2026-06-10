class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        starts = []
        for num in nums:
            
            m[num] = 1
        for k in m:

            if k-1 not in m:
                starts.append(k)
        # m {2:1, 20:1, 4:1, 10:1, 3:1, 4:1, 5:1}

        # loop through thte keys and add 1 to the key if it exist we increase consq, if not move to next key val
        res = 0 
        for key in starts:

            check = key
            currMax = 0
            while check in m:
      
                check += 1
                currMax += 1
                res = max(res, currMax)

        return res

