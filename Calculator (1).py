result = 0



def performOperation():
    if (operation == '+'):
        result = numberOne + numberTwo
        return result
    elif (operation == '-'):
        result = numberOne - numberTwo
        return result
    elif (operation == '*'):
        result = numberOne * numberTwo
        return result
    elif (operation == '/'):
        result = numberOne / numberTwo
        return result
    else:
        print("try again")
    

numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))
operation = input("Enter an operator (+ - * /): ")

result = performOperation()

print(str(numberOne) + " " + str(operation) + " " + str(numberTwo) + " = " + str(result))
