class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()
                if t == "+":
                    stack.append(left_operand + right_operand)
                elif t == "-":
                    stack.append(left_operand - right_operand)
                elif t == "/":
                    stack.append(int(float(left_operand)/right_operand))
                elif t == "*":
                    stack.append(left_operand * right_operand)
        
        return stack.pop()