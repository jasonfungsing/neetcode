class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = {x: 1 for x in range(len(nums))}
        for i, e in enumerate(nums):
            for k in d:
                if k != i:
                    d[k] = d[k] * e
        
        value_array = [d[k] for k in range(len(nums))]
        return value_array
        