def op1(num1, num2):
    return num1 * num2 / 100

def op2(num1, num2):
    return num1 / num2 * 100

def op3(num1, num2):
    return num1 / num2 * 100

def op4(num):
    return num / 100

operations = {
    '1': op1,
    '2': op2,
    '3': op3,
    '4': op4
}

while True:
    print(
        " 1. percent of a number\n",
        "2. percent of is number\n",
        "3. number is percent of\n",
        "4. Percent of a number\n")
    choice = input("Enter operation: ")
    if choice in operations:
        operation = operations[choice]


    if choice == '1':
        percent = int(input("Enter percent: "))
        number = int(input("Enter number: "))
        result = operation(percent, number)
        print(percent, "% for", number, "=", result)

    elif choice == '2':
        num1 = int(input("Enter first num: "))
        num2 = int(input("Enter second num: "))
        result = operation(num1, num2)
        print("What percent of", num1, "is", num2, "=", result, "%")

    elif choice == '3':
        num = int(input("Enter number: "))
        percent = int(input("Enter percent: "))
        result = operation(num, percent)
        print(num, "is", percent, "=", result)

    elif choice == '4':
        num = int(input("Enter number: "))
        result = operation(num)
        print("Result: ", result)
