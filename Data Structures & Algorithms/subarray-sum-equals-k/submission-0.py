class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefs = {}
        count = 0
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            if total == k:
                count += 1
            if total - k in prefs:
                count += prefs[total - k]
            # Update map
            prefs[total] = prefs.get(total, 0) + 1

        return count


        