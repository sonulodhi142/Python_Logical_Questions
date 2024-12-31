# program to find the palindrome number from the given number

#create variable to ger number
str = input("enter a num::")

# Reverse the number or string
palindrom = str[::-1]

# condition to check the number is palindrome or note
if palindrom == str:
    print(f"{palindrom } is the palindrom")
else:
    print(f"{str } is not the palindrom")
