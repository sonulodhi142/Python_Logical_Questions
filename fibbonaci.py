# the program of fibonaci series

num1 = 0
num2 = 1

# taking input of no. of terms
terms = int(input("Enter the number of terms::"))

# loop to swap the variable value and print the series

for i in range(1 , terms+1):
    print(num1)
    num1, num2 = num2, num1
    num1 += num2