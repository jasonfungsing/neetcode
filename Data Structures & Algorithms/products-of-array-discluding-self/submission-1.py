class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prep = []
        cp = 1
        for n in nums:
            cp = cp * n
            prep.append(cp)
        
        postp = []
        cp = 1
        for n in reversed(nums):
            cp = cp * n
            postp.insert(0, cp)
        
        value_array = []
        for i in range(len(nums)):
            value = 0
            # 0, 1, 2, 3 ---- len(4)
            # if i = 0, take the postP from 1 
            # if i(3) = len(nums) - 1, take the preP from i - 1
            # else prep i - 1 X post i + 1
            if i == 0:
                value = postp[1]
            elif i == len(nums) - 1:
                value = prep[i-1]
            else:
                value = prep[i-1] * postp[i+1]

            value_array.append(value)    
        return value_array
        