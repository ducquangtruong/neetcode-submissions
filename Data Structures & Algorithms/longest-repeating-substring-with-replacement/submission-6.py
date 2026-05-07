class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        start, end = 0, 0
        res = 0
        maxFreq = 0
        while end < len(s):
            cnt[s[end]] += 1
            maxFreq = max(maxFreq, cnt[s[end]])
            if end - start + 1 - maxFreq > k:
                res = max(res, end - start)
                while end - start + 1 - maxFreq > k:
                    cnt[s[start]] -= 1
                    start += 1
            end += 1
        
        return max(res, end - start)