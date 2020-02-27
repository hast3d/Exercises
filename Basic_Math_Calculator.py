
#Input a number an operator and another number
num1,operator,num2 = input().split(maxsplit=2)
num1 = int(num1)
num2 = int(num2)
#Check what operator to use anc calculate output

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/" and num2 != 0:
    print(num1 / num2)
elif  num2 == 0:
    print("Error: Division by zero!")



