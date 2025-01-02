# import a re module from python 
import re

# take a example Email
email = "test@example.com" 

# make a pattern to check the Gmail pattarn
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" 

# condition check
if re.match(pattern, email): 
    print("Valid email!") 
else: 
    print("Invalid email!")
