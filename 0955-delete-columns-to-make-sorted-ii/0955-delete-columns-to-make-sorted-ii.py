class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res, check = 0, [0 for _ in strs]
        for j in range(len(strs[0])):
            newOne = set()
            for i in range(1, len(strs)):
                if check[i] or strs[i][j] == strs[i-1][j]: 
                    continue
                elif strs[i][j] > strs[i-1][j]:
                    newOne.add(i)
                else:
                    res += 1
                    break
            else:
                for num in newOne:
                    check[num] = 1
        return res