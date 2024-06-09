class Solution:
    def findWinningPlayer(self, AA: List[int], k: int) -> int:
        A = Counter()
        B = deque([i for i in range(len(AA))])
        for _ in range(len(AA)):
            i, j = B.popleft(), B.popleft()
            if AA[i] > AA[j]:
                B.append(j)
                B.appendleft(i)
                A[i] += 1
                if A[i] == k: return i
            else:
                B.append(i)
                B.appendleft(j)
                A[j] += 1
                if A[j] == k: return j
        return B.popleft()