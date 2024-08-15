class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for token in tokens:
            if token =="+":
                summ = stack.pop() + stack.pop()
                stack.append(summ)
            elif token == "-":
                num2 = stack.pop()  
                num1 = stack.pop()  
                subb = num1 - num2 
                stack.append(subb)
            elif token == "*":
                prod = stack.pop() * stack.pop()
                stack.append(prod)
            elif token == "/":
                num2 = stack.pop()  
                num1 = stack.pop()
                divs = int(num1 / num2)
                stack.append(divs)
            else:
                stack.append(int(token))
        return  stack[0]
            


        