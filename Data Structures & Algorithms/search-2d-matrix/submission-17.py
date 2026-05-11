class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False

        row_l, row_r = 0, len(matrix)-1
        while row_r >= row_l:
            row_mid = (row_l + row_r) // 2
            print(row_l, row_mid, row_r)
            if matrix[row_mid][0] > target:
                if matrix[row_mid-1][0] < target:
                    row = matrix[row_mid-1]
                    break
                else:
                    row_r = row_mid - 1
            elif matrix[row_mid][0] < target:
                row_l = row_mid + 1
                row = matrix[row_mid]
            else:
                return True

        l, r = 0, len(row)-1
        while r >= l:
            mid = (l + r) // 2
            if row[mid] > target:
                r = mid - 1
            elif row[mid] < target:
                l = mid + 1
            else:
                return True
        return False
