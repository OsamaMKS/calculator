
def main():
	#write your code here
	num1 = input("Enter your first number :")
	oper = input("Enter the operation ( * , / , + , - ) :")
	num2 = input("Enter the second number :")
	ans = 0
	if num1.isdigit() == False or num2.isdigit() == False:
		print(" the numbers were invalid, Try again")
		main()

	if oper == "+":
		ans = int(num1) + int(num2)
		print("The add of your numbers is :" ,str(ans))
	elif oper == "-":
		ans = int(num1) - int(num2)
		print("The subtract of your number is: " , str(ans))
	elif oper == "*":
		ans = int(num1) * int(num2)
		print("The multi of your numbers is :" , str(ans))
	elif oper == "/" :
		ans = int(num1) / int(num2)
		print("The div of your numbers is :", str(ans))
	else :
		print("The operation is not valid , Try again")
		main()


if __name__ == '__main__':
	main()
