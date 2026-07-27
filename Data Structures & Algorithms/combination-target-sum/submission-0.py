class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(remaining, start_index, path):
            if remaining == 0:
                results.append(list(path))
                return
            if remaining < 0:
                return
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                dfs(remaining - nums[i], i, path)
                path.pop()

        dfs(target, 0, [])
        return results