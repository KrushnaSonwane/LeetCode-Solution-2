class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        dic, ans, un = {}, "", []
        for ch in s:
            if ch not in order:
                un.append(ch)
            if ch not in dic: 
                dic[ch] = 1
            else: dic[ch] += 1
        for ch in order:
            if ch in dic:
                ans += ch*dic[ch]
        for ch in un:
            ans += ch
        return ans