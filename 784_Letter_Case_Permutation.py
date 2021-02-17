class Solution:
    # permutation, dfs
    def letterCasePermutation(self, S: str) -> List[str]:
        if S.isdigit():
            return [S]
        res = []
        path = ""
        i = 0
        self.dfs(i, S, path, res)
        return res
    
    def dfs(self, i, S, path, res):
        if i == len(S):
            res.append(path)
            return
        if S[i].isdigit():
            self.dfs(i+1, S, path+S[i], res)
        else:
            self.dfs(i+1, S, path+S[i], res)
            self.dfs(i+1, S, path+S[i].swapcase(), res)