class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, matrix):
        # write your code here
        row, col, = len(matrix), len(matrix[0])
        lo, hi = 1, col-2
        while lo <= hi:
            mid = (lo+hi) // 2
            col_max, row_index = matrix[0][mid], 0
            for i in range(1, row-1):
                if matrix[i][mid] > col_max:
                    col_max = matrix[i][mid]
                    row_index = i
            if matrix[row_index][mid] < matrix[row_index][mid-1]:
                hi = mid - 1
            elif matrix[row_index][mid] < matrix[row_index][mid+1]:
                lo = mid + 1
            else:
                return (row_index, mid)