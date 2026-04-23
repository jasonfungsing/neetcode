class Solution:
    def isValid(self, s: str) -> bool:
        my_list = []
        for i in range(len(s)):
            item = s[i]
            if item == '[' or item =='{' or item == '(':
                my_list.append(item)
            else:
                if item == ']':
                    if my_list:
                        if my_list.pop() != '[':
                            return False
                    else:
                        return False
                if item == '}':
                    if my_list:
                        if my_list.pop() != '{':
                            return False
                    else:
                        return False
                if item == ')':
                    if my_list:
                        if my_list.pop() != '(':
                            return False
                    else:
                        return False
                
        if len(my_list) != 0:
            return False
        return True