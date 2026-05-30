class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # loop throguht the array -> append to a stack
        # stack = [1 2 ]
        # Once we get to an operator, do the operator on the items in the stack.
        # append the result to the stack 
        # continue until the end of the arry is met or the stack is == 1

        stack = []

        for n in tokens:
            if n == "*":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(n1 * n2)
            elif n == "+":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(n1 + n2)
            elif n == "-":
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                stack.append(int(n1 - n2))
            elif n == "/":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(int(n2 / n1))
            else:
                stack.append(int(n))

        return stack[0]
            


        