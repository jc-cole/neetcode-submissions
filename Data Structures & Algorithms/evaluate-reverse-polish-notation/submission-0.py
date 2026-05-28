import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        op_funcs = {
            "+": lambda x, y : x + y,
            "-": lambda x, y : x - y,
            "*": lambda x, y : x * y,
            "/": lambda x, y : math.trunc(x / y)
        }

        ops = op_funcs.keys()

        stack = []
        
        for symbol in tokens:
            if symbol in ops:
                right_op = int(stack.pop())
                left_op = int(stack.pop())
                stack.append(str(op_funcs[symbol](left_op, right_op)))
            else:
                stack.append(symbol)

        return int(stack[-1])