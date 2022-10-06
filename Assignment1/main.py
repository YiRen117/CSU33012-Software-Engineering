import calculator

if __name__ == '__main__':
    read = True
    while read:
        inputString = input("Please enter a mathematical expression: ")
        lst = calculator.readInput(inputString)
        if lst not in [-1, -2, -3, -4]:
            read = False
    sol = calculator.runCalculator(lst)
    print(sol)
