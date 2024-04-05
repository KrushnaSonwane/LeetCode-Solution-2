class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            else:
                if stack[-1].upper() == stack[-1]:
                    if ch.lower() == stack[-1].lower() and ch == ch.lower(): stack.pop()
                    else: stack.append(ch)
                else:
                    if ch.upper() == stack[-1].upper() and ch == ch.upper(): stack.pop()
                    else: stack.append(ch)
        return "".join(ch for ch in stack)