class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        taken = set()
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()

        # IDEA: Detect cycle in a directed graph
        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                if crs not in taken:
                    taken.add(crs)
                    res.append(crs)
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            preMap[crs] = []
            taken.add(crs)
            res.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res
