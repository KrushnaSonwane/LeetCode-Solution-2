from sortedcontainers import SortedList
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        A, B = SortedList(), SortedList()
        A.add(nums[0])
        B.add(nums[1])
        def getCount(Arr, key):
            i = bisect_right(Arr, key)
            return len(Arr)-i
        r1, r2 = [nums[0]], [nums[1]]
        for num in nums[2:]:
            a, b = getCount(A, num), getCount(B, num)
            if a > b:
                A.add(num)
                r1.append(num)
            elif b > a:
                B.add(num)
                r2.append(num)
            else:
                if len(A) > len(B):
                    r2.append(num)
                    B.add(num)
                else:
                    r1.append(num)
                    A.add(num)
        return r1 + r2
            