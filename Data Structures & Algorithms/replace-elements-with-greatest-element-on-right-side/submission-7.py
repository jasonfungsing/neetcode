class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for k,v in enumerate(arr):
            for i in range(len(result)):
                if result[i] < v:
                    result[i] = v
            result.append(-1)
        return result
        