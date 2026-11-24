class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        m = {}
        for str in strs:
            ca = [0] * 26
            for c in str:
                d = ord(c) - ord('a')
                ca[d] += 1
            fca = tuple(ca)
            if fca in m:
                m[fca].append(str)
            else:
                m[fca] = [str]
        
        return list(m.values())
        