class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)
        
        charCount = {}
        maxCharCount = 0
        l = 0
        res = 0

        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            maxCharCount = max(maxCharCount, charCount[s[r]])
            if (r - l + 1) - maxCharCount > k:
                charCount[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res