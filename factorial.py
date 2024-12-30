# factorial program using function

# function
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact    

num = int(input("Enter the number to find factorial::"))

print(factorial(num))