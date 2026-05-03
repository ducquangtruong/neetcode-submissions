class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = defaultdict(set)
        for key, val in prerequisites:
            preReq[key].add(val)
        
        q = deque()
        for course in range(numCourses):
            if course not in preReq:
                q.append(course)

        while q:
            cur = q.popleft()
            for key, vals in list(preReq.items()):
                if cur in vals:
                    vals.remove(cur)
                if len(vals) == 0:
                    q.append(key)
                    del preReq[key]
        
        return len(preReq) == 0