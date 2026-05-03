class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for s in strs:
            count = [0] * 26
            for chr in s:
                count[ord(chr) - ord('a')] += 1
            key = tuple(count)
            if key in table:
                table[key].append(s)
            else:
                table[key] = [s]
        
        res = []
        for key, value in table.items():
            res.append(value)
        
        return res