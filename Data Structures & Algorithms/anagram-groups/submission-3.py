class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        m = defaultdict(list)

        for word in strs:
            srt = sorted(word)

            m["".join(srt)].append(word)

        ans = []

        for key in m:
            ans.append(m[key])
        
        return ans