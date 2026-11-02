class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for op in operations:
            if op == "+":
                last_two_sum = sum(s[-2:])
                s.append(last_two_sum)
            elif op == "D":
                twice_of_last_one = 2 * s[-1]
                s.append(twice_of_last_one)
            elif op == "C":
                s.pop()
            else:
                s.append(int(op))
        return sum(s)
