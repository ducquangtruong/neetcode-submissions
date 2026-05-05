"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: [x.start, x.end])
        stk = []
        for interval in intervals:
            if not stk:
                last_end = -1
            else:
                last_end = stk[-1].end
            if interval.start < last_end:
                return False
            stk.append(interval)
        
        return True