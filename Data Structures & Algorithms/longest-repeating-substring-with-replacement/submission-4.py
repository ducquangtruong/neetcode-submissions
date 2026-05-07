class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = [0] * 26
        start, end = 0, 0
        res = 0
        while end < len(s):
            cnt[ord(s[end]) - ord('A')] += 1
            if end - start + 1 - max(cnt) > k:
                res = max(res, end - start)
                while end - start + 1 - max(cnt) > k:
                    cnt[ord(s[start]) - ord('A')] -= 1
                    start += 1
            end += 1
        
        return max(res, end - start)