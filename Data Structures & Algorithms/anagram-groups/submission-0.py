class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for string in strs:
            key = "".join(sorted(list(string)))
            table.setdefault(key, [])
            table[key].append(string)
        return table.values()