# function to print a rectangle of stars

def rectangle(lines):
    for i in range(1,lines+1):
        if i==1 or i== lines:
            print("*"*lines)
        else:
            print("*"+" "*(lines-2)+" *")

rectangle(7)