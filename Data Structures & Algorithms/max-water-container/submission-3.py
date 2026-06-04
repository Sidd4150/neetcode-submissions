class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) -1

        currMax = 0

        while l < r :
            m = min(heights[l], heights[r])
            currMax = max(currMax, m * (r - l) )

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return currMax
