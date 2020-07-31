def op1(num1, num2):
	return number * percent / 100
def op2(num1, num2):
	return num1 / num2 * 100
def op3(num1, num2):
	return num1 / num2 * 100
def op4(num):
	return num / 100
op = 1
chr(op)

print(" 1. percent of a number \n \
2. percent of is number \n \
3. number is percent of \n \
4. Percent of a number \n")

choice = input("Enter opertation: ")
while(op != 'e'):
	if choice == '1':
		#op1
		percent = int(input("Enter percent: "))
		number = int(input("Enter number: "))
		result = print(percent, "%", "for", number, "=", op1(percent, number))
		print("Are u want to continue, y or n?")
		choice = input("Enter opertation: ")
		while True:
			if choice == 'y': 
				percent = int(input("Enter percent: "))
				number = int(input("Enter number: "))
				result = print(percent, "%", "for", number, "=", op1(percent, number))
				print("Are u want to continue, Y or N ?")
				choice = input("Enter opertation: ")
			break	
		if choice == 'n':
			print(" 1. percentage of a number, \n 2. What percent of is, \n 3. What number of percent is, \n 4. Percent of a number,")
			choice = input("Enter operation: ")
	elif choice == '2':
		#op2
		num1 = int(input("Enter first num: "))
		num2 = int(input("Enter second num: "))
		result = print("What percent of", num1, "is", num2, "=", op2(num1, num2), "%")
		print("Are u want to continue, y or n?")
		choice = input("Enter opertation: ")
		while True:
			if choice == 'y':
				percent = int(input("Enter percent: "))
				number = int(input("Enter number: "))
				result = print(percent, "%", "for", number, "=", op1(percent, number))
				print("Are u want to continue, Y or N ?")
				choice = input("Enter opertation: ")
			break	
		if choice == 'n':
			print(" 1. percentage of a number, \n 2. What percent of is, \n 3. What number of percent is, \n 4. Percent of a number,")
			choice = input("Enter operation: ")
	elif choice == '3':
		#op3
		num = int(input("Enter number: "))
		percent = int(input("Enter percent: "))
		result = print(num, "is", percent, "=", op3(num, percent))
		print("Are u want to continue, y or n?")
		choice = input("Enter opertation: ")
		while True:
			if choice == 'y': 
				percent = int(input("Enter percent: "))
				number = int(input("Enter number: "))
				result = print(percent, "%", "for", number, "=", op1(percent, number))
				print("Are u want to continue, Y or N ?")
				choice = input("Enter opertation: ")
			break	
		if choice == 'n':
			print(" 1. percentage of a number, \n 2. What percent of is, \n 3. What number of percent is, \n 4. Percent of a number,")
			choice = input("Enter operation: ")
	elif choice == '4':
		#op4
		num = int(input("Enter number: "))
		result = print("Here is percent of this number ->", op4(num))
		print("Are u want to continue, y or n?")
		choice = input("Enter opertation: ")
		while True:
			if choice == 'y': 
				percent = int(input("Enter percent: "))
				number = int(input("Enter number: "))
				result = print(percent, "%", "for", number, "=", op1(percent, number))
				print("Are u want to continue, Y or N ?")
				choice = input("Enter opertation: ")
			break	
		if choice == 'n':
			print(" 1. percentage of a number, \n 2. What percent of is, \n 3. What number of percent is, \n 4. Percent of a number,")
			choice = input("Enter operation: ")	
