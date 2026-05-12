class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS*COLLS - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid // COLLS][mid % COLLS] > target:
                r = mid - 1
            elif matrix[mid //COLLS][mid % COLLS] < target:
                l = mid + 1
            else:
                return True
        return False