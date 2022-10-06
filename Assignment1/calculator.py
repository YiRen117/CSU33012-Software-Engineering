import re
from queue import LifoQueue

def readInput(inputStr):
    # check if unexpected character exists
    for ch in inputStr:
        if ch not in ["0","1","2","3","4","5","6","7","8","9","+","-","*"," "]:
            print("Error: unexpected character.")
            return -1
    # set a list containing all operands and operators
    lst = re.findall(r"\d+|[+\-*]", inputStr)
    # check for missing operands
    if lst[0] in ["+", "*"] or lst[len(lst)-1] in ["+","-","*"] or (lst[0]=="-" and lst[1] in ["+","-","*"]):
        print("Error: Missing operands.")
        return -2
    # check for duplicated operands or operators
    digtNext = True
    minus = False
    for i, item in enumerate(lst):
        if item.isdigit() != digtNext:
            if digtNext:
                if item != "-":
                    print("Error: Duplicated operators.")
                    return -3
                else:
                    minus = True
                    lst[i] = "n"
            else:
                print("Error: Duplicated operands.")
                return -4
        else:
            if digtNext and minus:
                lst[i] = "-" + item
                minus = False
            digtNext = not digtNext
    # return the list if the expression is valid
    nclear = False
    while not nclear:
        if "n" not in lst:
            nclear = True
        else:
            lst.remove("n")
    return lst

def calculate(num1, operator, num2):
    if operator == "+":
        return str(int(num1) + int(num2))
    elif operator == "-":
        return str(int(num1) - int(num2))
    else:
        return str(int(num1) * int(num2))

def infixToPostfix(infixlst):
    # initialize a stack
    stack = LifoQueue()
    stacktop = 0
    postfixlst = []
    precedence = {"+":1, "-":1, "*":2}
    for item in infixlst:
        if item.isdigit() or item.lstrip("-").isdigit():
            postfixlst.append(item)
        else:
            if not stack.empty() and precedence[item] <= stacktop:
                while not stack.empty():
                    postfixlst.append(stack.get())
                stack.put(item)
                stacktop = precedence[item]
            else:
                stack.put(item)
                stacktop = precedence[item]
    while not stack.empty():
        postfixlst.append(stack.get())
    return postfixlst

def runCalculator(lst):
    postfixlst = infixToPostfix(lst)
    stack = LifoQueue()
    solution = 0
    if len(lst) == 1:
        return lst[0]
    for item in postfixlst:
        if item.isdigit() or item.lstrip("-").isdigit():
            stack.put(item)
        else:
            num2 = stack.get()
            num1 = stack.get()
            solution = calculate(num1, item, num2)
            stack.put(solution)
    return solution
