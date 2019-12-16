"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
"""
def evalRPN(tokens):
    stack = []
    for i in tokens:
        if i=="+" or i=="-" or i=="*" or i=="/":
            a = int(stack.pop())
            b = int(stack.pop())
            if i=="+":
                c = a+b
            elif i=="-":
                c = b-a
            elif i=="*":
                c = b*a
            elif i=="/":
                c = int(b/a)
            stack.append(c)
        else:
            stack.append(i)
    return stack[0]

res = evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
print(res)
