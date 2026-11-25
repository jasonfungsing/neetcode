class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest_streak = 0
        if len(nums) == 0:
            return longest_streak
        s = set(nums)
        while s:
            n = s.pop()
            longest_streak = max(longest_streak, 1)
            left = n-1
            while left in s:
                s.remove(left)
                left = left - 1
            right = n + 1
            while right in s:
                s.remove(right)
                right = right + 1
            longest_streak = max(longest_streak, right-left-1)
            if longest_streak >= len(s):
                break

        return longest_streak
        