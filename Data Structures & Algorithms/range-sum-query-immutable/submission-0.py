class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        i, total = 0, 0
        while i < len(nums):
            total += nums[i]
            self.prefixSum.append(total)
            i += 1
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right] - (self.prefixSum[left-1] if left > 0 else 0)