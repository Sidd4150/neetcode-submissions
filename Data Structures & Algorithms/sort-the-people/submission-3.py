class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        m = defaultdict(str)

        for i in range(len(names)):

            m[heights[i]] = names[i]

        heights.sort()
        ans = []
        for height in heights[::-1]:
            ans.append(m[height])

        return ans