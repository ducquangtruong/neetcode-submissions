class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countTasks = Counter(tasks)
        hq = []
        for task, cnt in countTasks.items():
            heapq.heappush(hq, [0, -cnt, task])
        res = 0
        while hq:
            time, negCnt, task = hq[0]
            if time <= res:
                heapq.heappop(hq)
                negCnt += 1
                if negCnt != 0:
                    heapq.heappush(hq, [time + n + 1, negCnt, task])
            res += 1
        return res