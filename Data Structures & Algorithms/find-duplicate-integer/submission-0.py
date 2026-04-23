class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f = None
        result = None
        while True:
            cv = nums[0]
            fv = nums[cv]
            if cv == fv:
                result = cv
                break
            else:
                nums[cv] = cv
                nums[0] = fv
        
        return result



        