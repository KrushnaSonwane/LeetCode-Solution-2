class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        count = 0
        ans = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
                count += 1
            elif ch == ')':
                count -= 1
                stack.pop()
            ans = max(ans, count)
        return ans