class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        tmp = 0
        for n in nums:
            if n == 1:
                tmp += 1
                result = max(result, tmp)
            else:
                tmp = 0
        return result

        