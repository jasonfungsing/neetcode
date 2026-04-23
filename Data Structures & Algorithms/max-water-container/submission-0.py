class Solution:
    def maxArea(self, height: List[int]) -> int:
        L,R = 0, len(height) - 1
        area = 0
        while L < R:
            cL, cR = height[L],height[R]
            current = (R - L) * min(cL, cR)
            area = max(current, area)

            if height[L] >= height[R]:
                while R > L:
                    R -= 1
                    if height[R] > cR:
                        break
            else:
                while L < R:
                    L += 1
                    if height[L] > cL:
                        break
        return area