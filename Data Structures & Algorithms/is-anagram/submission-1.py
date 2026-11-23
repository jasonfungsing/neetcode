import numpy as np

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for j in t:
            if j in d:
                d[j] -= 1
            else:
                d[j] = -1

        one = set(d.values())
        return one == {0}
        
        
        