# factorial using recursion fuction in python
def factorial(n):
    
    if n == 1:
        return 1
    return n * factorial(n-1)

num = int(input("Enter the number to find factorial::"))

print(factorial(num))