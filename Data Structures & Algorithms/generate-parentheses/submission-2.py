class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(opn, cls, cur):
            if cls == 0:
                res.append(cur)
                return
            
            if opn > 0:
                dfs(opn - 1, cls, cur + "(")
            if cls > opn:
                dfs(opn, cls - 1, cur + ")")
            
        dfs(n, n, "")
        return res