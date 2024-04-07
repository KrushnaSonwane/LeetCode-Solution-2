class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs(i, count):
            if count == -1: return False
            if i == len(s):
                return count == 0
            if s[i] == '(':
                return dfs(i+1, count+1)
            elif s[i] == ')':
                return dfs(i+1, count-1)
            return dfs(i+1, count+1) or dfs(i+1, count-1) or dfs(i+1, count)
        return dfs(0, 0)
