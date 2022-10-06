import calculator

if __name__ == '__main__':
    inputString = input("Please enter a mathematical expression: ")
    sol = calculator.runCalculator(inputString)
    print(sol)
