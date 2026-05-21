class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCnts = Counter(tasks)

        # Idea: Push the task onto a queue until they are ready
        maxHeap = [taskCnt for taskCnt in taskCnts.values()]
        heapq.heapify_max(maxHeap)

        q = deque()
        time = 0
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                taskCnt = heapq.heappop_max(maxHeap) - 1
                if taskCnt:
                    q.append([taskCnt, time + n])
            # If task is ready, add back into heap
            if q and q[0][1] == time:
                taskCnt, _ = q.popleft()
                heapq.heappush_max(maxHeap, taskCnt)

        return time