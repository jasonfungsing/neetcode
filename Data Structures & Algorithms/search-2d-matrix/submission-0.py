class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.rhelper(matrix, 0, len(matrix)-1, target)
        if row != -1:
            return self.chelper(matrix, row, 0, len(matrix[row])-1, target)
        else:
            return False

    def rhelper(self, matrix: List[List[int]], rsi: int, rei: int, target: int) -> int:
        if matrix[rsi][0] <= target <= matrix[rsi][-1]:
            return rsi
        if matrix[rei][0] <= target <= matrix[rei][-1]:
            return rei
        if rei - rsi > 1:
            rm = (rsi + rei) // 2
            if matrix[rm][0] > target:
                return self.rhelper(matrix, rsi, rm - 1, target)
            elif matrix[rm][-1] < target:
                return self.rhelper(matrix, rm + 1, rei, target)
            else:
                return rm
        return -1
    

    def chelper(self, matrix: List[List[int]], row: int, csi: int, cei: int, target: int) -> bool:
        if csi <= cei:
            cm = (csi + cei) // 2
            if matrix[row][cm] == target:
                return True
            elif matrix[row][cm] > target:
                return self.chelper(matrix, row, csi, cm - 1, target)
            else:
                return self.chelper(matrix, row, cm + 1, cei, target)
        return False
