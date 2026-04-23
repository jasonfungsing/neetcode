class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insertIndex = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        return insertIndex
        