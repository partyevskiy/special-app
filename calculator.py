a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
do = input("Enter operation: ")
if do == "*":
	print(a, "*", b, "=", a * b)
elif do == "/":
	print(a, "/", b, "=", a / b)
elif do == "+":
	print(a, "+", b, "=", a + b)
elif do == "-":
	print(a, "-", b, "=", a - b)
else:
	print("Enter error!")