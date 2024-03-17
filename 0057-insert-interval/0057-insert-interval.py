class Solution:
    def insert(self, inter: List[List[int]], new: List[int]) -> List[List[int]]:
        flag = False
        res = []
        for li in inter:
            if not flag:
                if li[0] > new[1]:
                    res.append(new)
                    res.append(li)
                    flag = True
                elif li[1] < new[0]:
                    res.append(li)
                elif new[0] >= li[0] and new[1] >= li[1]:
                    res.append([min(new[0], li[0]), max(new[1], li[1])])
                    flag = True
                elif new[0] >= li[0] and new[0] <= li[1]:
                    res.append([min(new[0], li[0]), max(new[1], li[1])])
                    flag = True
                elif li[0] >= new[0] and li[0] <= new[1]:
                    res.append([min(new[0], li[0]), max(new[1], li[1])])
                    flag = True
            else:
                if res[-1][0] <= li[0] and li[0] <= res[-1][1]:
                    res[-1][0] = min(res[-1][0], li[0])
                    res[-1][1] = max(res[-1][1], li[1])
                elif li[0] >= res[-1][0] and li[1] <= res[-1][1]:
                    res[-1][0] = min(res[-1][0], li[0])
                    res[-1][1] = max(res[-1][1], li[1])
                elif li[0] <= res[-1][0] and res[-1][1] >= li[0]:
                    res[-1][0] = min(res[-1][0], li[0])
                    res[-1][1] = max(res[-1][1], li[1])
                else:
                    res.append(li)
        if not flag: res.append(new)
        return res