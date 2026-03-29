class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for n in row:
                if target == n:
                    return True

        return False
        