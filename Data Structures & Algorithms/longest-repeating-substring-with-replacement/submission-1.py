class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = list(s)
        d = {}
        L = 0
        length = 0

        for R in range(len(a)):
            if a[R] in d:
                d[a[R]] += 1
            else:
                d[a[R]] = 1
            
            all_values = list(d.values())
            max_value = max(all_values)
            total_without_max = sum(all_values) - max_value
            
            if total_without_max > k:
                if d[a[L]] == 1:
                    del d[a[L]]
                else:
                    d[a[L]] -= 1
                L += 1
            else:
                length = max(length, sum(all_values))
        
        return length

        # AABACBC E 4
        # {A:3, B:2, C:2, }
        # dict value total is the length
        # dict value total - k 