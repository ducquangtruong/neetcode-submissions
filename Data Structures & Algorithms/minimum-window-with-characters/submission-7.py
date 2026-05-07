class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # Initialize counter for t
        cnt_t = defaultdict(int)
        for chr in t:
            cnt_t[chr] += 1
        
        start, end = 0, 0
        res_start, res_end = -1, -1
        resLen = float('inf')
        have, need = 0, len(cnt_t)
        cnt_s = defaultdict(int)

        while end < len(s):
            cnt_s[s[end]] += 1
            if s[end] in cnt_t and cnt_s[s[end]] == cnt_t[s[end]]:
                have += 1

            # Shrink the window once the requirement is met
            while have == need:
                curr = end - start + 1
                if resLen > curr:
                    resLen = curr
                    res_start, res_end = start, end
                cnt_s[s[start]] -= 1
                if cnt_s[s[start]] < cnt_t[s[start]]:
                    have -= 1

                start += 1
            
            end += 1
        
        return s[res_start : res_end + 1] if resLen != float("inf") else ""