class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l = 0
        r = row - 1
        selected_row = None

        # find the row in which target exists
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][col-1]:
                selected_row = mid
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1 
        if selected_row is None:
            return False

        # search in the selected row
        l = 0
        r = col - 1

        while l<= r:
            mid = (l+r)//2
            if matrix[selected_row][mid] == target:
                return True
            elif matrix[selected_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
            