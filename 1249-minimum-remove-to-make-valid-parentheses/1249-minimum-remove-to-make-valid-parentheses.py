class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove, stack = set(), []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if not stack:
                    remove.add(i)
                else:
                    stack.pop()
        for i in stack:
            remove.add(i)
        return ''.join(s[i] for i in range(len(s)) if i not in remove)