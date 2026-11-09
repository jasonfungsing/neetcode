class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, len(nums) - 1, target)

    def helper(self, nums:List[int], start: int, end:int ,target) -> int:
        if end - start <= 1:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            else:
                return -1
        
        mid = int((start + end)/2)
        if target < nums[mid]:
            return self.helper(nums, start, mid, target)
        else:
            return self.helper(nums, mid, end, target)