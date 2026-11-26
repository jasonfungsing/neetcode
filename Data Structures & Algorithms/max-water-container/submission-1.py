class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        max_height = max(height)

        while left < right:
            dis = right - left
            if result >= dis * max_height:
                break
            left_h = height[left]
            right_h = height[right]
            if left_h >= right_h:
                cur_area = dis * right_h
                right -= 1
                while height[right] < right_h and left < right:
                    right -= 1
            else:
                cur_area = dis * left_h
                left += 1
                while height[left] < left_h and left < right:
                    left += 1
            if cur_area > result:
                result = cur_area
        return result
