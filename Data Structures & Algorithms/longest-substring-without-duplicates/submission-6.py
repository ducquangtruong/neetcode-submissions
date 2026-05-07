class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        start, end = 0, 0
        res = 0
        seen = defaultdict(int)
        while end < len(s):
            if s[end] in seen:
                res = max(res, end - start)
                new_start = seen[s[end]]
                while start <= new_start:
                    del seen[s[start]]
                    start += 1
            
            seen[s[end]] = end
            end += 1
        
        return max(res, end - start)