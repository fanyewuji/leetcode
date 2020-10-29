class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        # binary search to find the row idx
        l, h = 0, m-1
        row = 0
        while l <= h:
            mid = l + (h-l)//2
            if target <= matrix[mid][n-1] and target >= matrix[mid][0]:
                row = mid
                break
            elif target < matrix[mid][0]:
                    h -= 1
            else:
                l += 1
        print(row)
        # if n == 1:
        #     if matrix[row][0] == target:
        #         return True
        #     else:
        #         return False
        # use binary search to find the column idx
        l, h = 0, n
        while l < h:
            mid = l + (h-l)//2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l += 1
            else:
                h -= 1
        return False
        