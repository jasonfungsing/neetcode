class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = 0,0
        L,R = 0,len(height)-1
        i = L
        c = [0] * len(height)
        while L < R:
            maxL = max(maxL, height[L])
            maxR = max(maxR, height[R]) 
            h = min(maxL, maxR) - height[i]
            c[i] = max(0, h)
            if height[L] >= height[R]:
                R -= 1
                i = R
            else:
                L += 1
                i = L
        return sum(c)