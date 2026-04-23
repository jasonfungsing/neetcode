class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.m = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            linesum = 0
            for j in range(cols):
                linesum += matrix[i][j]
                self.m[i][j] = linesum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        totalSum = 0
        # matrix[row_index][column_index] 
        for i in range(row1, row2 + 1):
            totalSum += self.m[i][col2]
            if col1 > 0:
                totalSum -= self.m[i][col1-1]
        
        return totalSum