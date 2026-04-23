class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        myset = set()
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if num not in myset:
                myset.add(num)
            else:
                del nums[i]
        return len(myset)

        