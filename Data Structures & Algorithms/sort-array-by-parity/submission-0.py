class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        ans = []
        odd = []
        for n in nums:
            if n % 2 == 0:
                ans.append(n)
            else:
                odd.append(n)
       
        ans += odd
        return ans