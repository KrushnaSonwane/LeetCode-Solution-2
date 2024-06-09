class Solution:
    def clearDigits(self, s: str) -> str:
        Q = []
        for ch in s:
            if ch.isdigit():
                Q.pop()
            else:
                Q.append(ch)
        return ''.join(Q)