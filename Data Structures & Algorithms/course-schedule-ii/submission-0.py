class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #adj list
        m = defaultdict(list)
        vis,cycle = set(),set()
        output = []

        for u,v in prerequisites:
            m[u].append(v)


        def dfs(crs):
            if crs in cycle:
                return False

            if crs in vis:
                return True

            cycle.add(crs)

            for nei in m[crs]:
                if not dfs(nei):
                    return False

            cycle.remove(crs)
            vis.add(crs)
            output.append(crs)

            
            return True

  
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output

     

