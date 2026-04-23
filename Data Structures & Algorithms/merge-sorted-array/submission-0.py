class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        i2 = 0
        y = 0
        while i1 < m + y and i2 < n:
            n1 = nums1[i1]
            n2 = nums2[i2]
            if n2 <= n1:
                nums1.insert(i1, n2)
                nums1.pop()
                y += 1
                i1 += 1
                i2 += 1
            else:
                i1 += 1
        nums1[m + y:] = nums2[y:]