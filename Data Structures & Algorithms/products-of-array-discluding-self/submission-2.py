class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = len(nums)
        answer = [1] * l
        prep = 1
        for i in range(l):
            answer[i] = prep
            prep *= nums[i]
        postp = 1
        for i in range(l-1, -1, -1):
            answer[i] *= postp
            postp *= nums[i]
        return answer