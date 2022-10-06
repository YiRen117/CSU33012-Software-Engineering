import re
from queue import LifoQueue

def readInput(inputStr):
    # check if unexpected character exists
    for ch in inputStr:
        if ch not in ["0","1","2","3","4","5","6","7","8","9","+","-","*"," "]:
            print("Error: unexpected character.")
            exit()
    # set a list containing all operands and operators
    lst = re.findall(r"\d+|[+\-*]", inputStr)
    # check for duplicated operands or operators
    digtNext = True
    for item in lst:
        if item.isdigit() != digtNext:
            if digtNext:
                print("Error: Duplicated operators.")
            else:
                print("Error: Duplicated operands.")
            exit()
        else:
            digtNext = not digtNext
    # return the list if the expression is valid
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
        if item.isdigit():
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

def runCalculator(inputString):
    lst = readInput(inputString)
    postfixlst = infixToPostfix(lst)
    stack = LifoQueue()
    solution = 0
    for item in postfixlst:
        if item.isdigit():
            stack.put(item)
        else:
            num2 = stack.get()
            num1 = stack.get()
            solution = calculate(num1, item, num2)
            stack.put(solution)
    return solution
