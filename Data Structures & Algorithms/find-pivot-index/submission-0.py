class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        postfs = []
        t = 0
        for y in range(len(nums) - 1, -1, -1):
            t += nums[y]
            postfs.insert(0, t)
        postfs.insert(0, t)
        t = 0
        index = -1

        for i in range(len(nums)):
            t += nums[i]
            if postfs[i+1] == t:
                index = i
                break
        
        return index





        