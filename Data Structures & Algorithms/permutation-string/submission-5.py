class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Frequency array for s1
        # Array instead of dict because only 26 letters
        # We do this because comparing arrays is faster
        cnt1 = [0] * 26
        for chr in s1:
            cnt1[ord(chr) - ord('a')] += 1

        cnt2 = [0] * 26
        start, end = 0, 0

        while end < len(s2):
            if end - start == len(s1):
                if cnt1 == cnt2:
                    return True
                cnt2[ord(s2[start]) - ord('a')] -= 1
                start += 1
            cnt2[ord(s2[end]) - ord('a')] += 1
            end += 1
        
        return cnt1 == cnt2
