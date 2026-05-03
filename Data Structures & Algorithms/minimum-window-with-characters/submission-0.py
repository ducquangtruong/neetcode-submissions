class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        count_t, window = Counter(t), {}
        cur_count, required_count = 0, len(count_t)
        res, res_len = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and window[c] == count_t[c]:
                cur_count += 1
            
            while cur_count == required_count:
                if (r - l + 1) < res_len:
                    res, res_len = [l, r], r - l + 1
                
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    cur_count -= 1
                
                l += 1
        l, r = res
        return s[l : r + 1] if res_len != float("infinity") else ""
        