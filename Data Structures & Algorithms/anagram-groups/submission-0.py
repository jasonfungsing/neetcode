class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            #ss = "".join(sorted(s))
            ss = self.convertStringToArray(s)
            if ss in d:
                d[ss].append(s)
            else:
                d[ss] = [s]
        return list(d.values())
    
    def convertStringToArray(self, s:str) -> List[int]:
        l = [0] * 26
        for c in s:
            l[ord(c) - ord('a')] += 1
        return tuple(l)



        