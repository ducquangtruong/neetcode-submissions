class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Frequency table for s1
        cnt1 = defaultdict(int)
        for chr in s1:
            cnt1[chr] += 1

        cnt2 = defaultdict(int)
        start, end = 0, 0

        while end < len(s2):
            if end - start == len(s1):
                print(start, end, cnt1, cnt2)
                if cnt1 == cnt2:
                    return True
                cnt2[s2[start]] -= 1
                if cnt2[s2[start]] == 0:
                    del cnt2[s2[start]]
                start += 1
            cnt2[s2[end]] += 1
            end += 1
        
        return cnt1 == cnt2