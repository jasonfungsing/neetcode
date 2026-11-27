class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        area = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                area += left_max - height[left]
                left += 1
            else:
                area += right_max - height[right]
                right -= 1
        return area
