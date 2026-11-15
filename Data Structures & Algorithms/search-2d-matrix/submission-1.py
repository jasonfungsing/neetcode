class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = [element for row in matrix for element in row]
        return self.chelper(arr, 0, len(arr)-1, target)

    def chelper(self, arr: [int], si: int, ei: int, target: int) -> bool:
        if si <= ei:
            cm = (si + ei) // 2
            if arr[cm] == target:
                return True
            elif arr[cm] > target:
                return self.chelper(arr, si, cm - 1, target)
            else:
                return self.chelper(arr, cm + 1, ei, target)
        return False
