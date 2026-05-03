class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        seen = set()
        l, r = 0, 0
        res = 0

        while r < len(s):
            if s[r] in seen:
                while l < r and s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        
        return max(res, r - l)
