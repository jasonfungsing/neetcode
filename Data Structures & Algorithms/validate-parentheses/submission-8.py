class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')':'(', '}':'{', ']':'['}
        result = True
        for c in s:
            if c not in d:
                stack.append(c)
            else:
                if len(stack) == 0:
                    result = False
                    break
                else:
                    if d[c] != stack.pop():
                        result = False
                        break

        if len(stack) !=0 and result:
            result = False
        return result


        