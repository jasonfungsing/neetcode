class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for k,v in enumerate(nums):
            ans[k] = v
            ans[k+n] = v
        return ans
        