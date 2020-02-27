
# Get 3 numbers form the user.

num1, num2, num3 = map(int, input().split())
smallest = 0

#Assign smallest number to smallest and print it.

if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <=num1 and num2 <=num3:
    smallest = num2
else:
    smallest = num3

print(smallest)
