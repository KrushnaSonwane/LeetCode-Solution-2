class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(ss):
            dp = [0 for _ in ss]
            for i in range(1, len(ss)):
                last = dp[i-1]
                while last > 0 and ss[last] != ss[i]:
                    last = dp[last-1]
                dp[i] = last + int(ss[last] == ss[i])
            return dp
        A = kmp(a+"#"+s)[len(a)+1:]
        B = kmp(b+'#'+s)[len(b)+1:]
        A = [i-(len(a)-1) for i in range(len(A)) if A[i] >= len(a)]
        B = [i-(len(b)-1) for i in range(len(B)) if B[i] >= len(b)]
        res = []
        for num in A:
            j = bisect_right(B, num-1)
            if j < len(B) and k >= abs(num-B[j]) or (j-1 >= 0 and k >= abs(num-B[j-1])):
                res.append(num)
        return res