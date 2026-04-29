class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0 
        num = n
        vis = set()
        while total != 1:
            total = 0
            for val in str(num):
                total += int(val)**2
            if total in vis:
                return False
            vis.add(total)

            num = total 
            


        return True
   