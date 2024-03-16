class Solution:
    def minimizeStringValue(self, s: str) -> str:
        hashT = {ch: 0 for ch in 'abcdefghijlkmnopqrstuvwxyz'}
        for ch in s:
            if ch != '?':
                hashT[ch] += 1
        A = []
        for ch in hashT:
            heappush(A, [hashT[ch], ch])
            # hashT[ch] = 
        res = []
        count = Counter()
        for ch in s:
            if ch == '?':
                cc, char = heappop(A)
                count[char] += 1 
                heappush(A, [cc+1, char])
        A = []
        for ch in count:
            heappush(A, [ch, count[ch]])
        for ch in s:
            if ch == '?':
                char, cc = heappop(A)
                res.append(char)
                if cc - 1 >= 1:
                    heappush(A, [char, cc-1])
            else:
                res.append(ch)
        return ''.join(res)