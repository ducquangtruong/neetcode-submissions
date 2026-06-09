class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        res = []
        numToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(cur, i):
            if i == len(digits):
                res.append(cur)
                return

            for c in numToLetters[digits[i]]:
                dfs(cur + c, i + 1)

        dfs("", 0)
        return res