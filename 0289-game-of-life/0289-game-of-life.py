class Solution:
    def gameOfLife(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        A = []
        for i in range(len(nums)):
            t, count = [], 0
            for j in range(len(nums[0])):
                count = 0
                for x, y in [(i,j+1), (i,j-1), (i+1,j), (i-1, j), (i-1,j+1), (i-1,j-1), (i+1,j-1), (i+1,j+1)]:
                    if 0 <= x < len(nums) and 0 <= y < len(nums[0]):
                        count += nums[x][y]
                if nums[i][j]:
                    t.append(0 if count < 2 or count > 3 else 1)
                else:
                    t.append(1 if count == 3 else 0)
            A.append(t)
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                nums[i][j] = A[i][j]