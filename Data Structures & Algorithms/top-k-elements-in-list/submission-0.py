class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        arr = [set() for _ in range(len(nums) + 1)]
        for key,value in d.items():
            arr[value].add(key)
 
        result = []
        for i,v in reversed(list(enumerate(arr))):
            if len(result) < k and v:
                result.extend(v)
        return result        