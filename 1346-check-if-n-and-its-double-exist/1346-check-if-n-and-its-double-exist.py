class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        for i, num in enumerate(arr):
            l, r = i + 1, len(arr) - 1
            if 0 > num:
                r = i - 1
                l = 0
            key = num * 2
            while r >= l:
                mid = (r + l) // 2
                if arr[mid] == key: return True
                if arr[mid] > key:
                    r = mid - 1
                else:
                    l = mid + 1
        return False