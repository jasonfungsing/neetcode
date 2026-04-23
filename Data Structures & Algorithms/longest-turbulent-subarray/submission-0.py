class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        total = 1
        curtotal = 1
        nextup = None
        for i in range(len(arr)):
            cur = arr[i]    
            if i > 0:
                pre = arr[i-1]
                if nextup == None:
                    if cur < pre:
                        nextup = True
                        curtotal += 1
                        total = max(total, curtotal)
                    elif cur > pre:
                        nextup = False
                        curtotal += 1
                        total = max(total, curtotal)
                else:
                    if cur < pre:
                        if nextup == False:
                            curtotal += 1
                            total = max(total, curtotal)
                            nextup = True
                        else:
                            nextup = True
                            curtotal = 2
                    elif cur > pre:
                        if nextup == False:
                            nextup = False
                            curtotal = 2
                        else:
                            curtotal += 1
                            total = max(total, curtotal)
                            nextup = False
                    else:
                        nextup = None
                        curtotal = 1
        return total
            
        