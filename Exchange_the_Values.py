
# Get two numbers
num_A, num_B = map(int, input().split())

# Exchange the numbers

num_C = num_A
num_A = num_B
num_B = num_C

print(num_A,num_B)