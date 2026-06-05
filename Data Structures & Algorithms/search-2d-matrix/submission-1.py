class Solution:
    def searchRow(self, matrix: List[List[int]], target: int) -> int:
        low_row = 0
        high_row = len(matrix) - 1
        while low_row <= high_row:
            mid_row = (low_row + high_row) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                return mid_row
            elif target < matrix[mid_row][0]:
                high_row = mid_row - 1
            elif target > matrix[mid_row][-1]:
                low_row = mid_row + 1
        return -1

    def searchCol(self, row: List[int], target: int) -> bool:
        low = 0
        high = len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif target < row[mid]:
                high = mid - 1
            elif target > row[mid]:
                low = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        target_in_row = self.searchRow(matrix, target)

        if target_in_row == -1:
            return False

        return self.searchCol(matrix[target_in_row], target)


        