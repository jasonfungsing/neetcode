class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i1, i2 = 0,len(numbers)-1
        while i1 < i2:
            sum = numbers[i1] + numbers[i2]
            if  sum < target:
                i1 += 1
            elif sum == target:
                break
            else:
                i2 -= 1

        return [i1+1, i2+1]