a = int(input("Enter your First number. \n"))
b = int(input("Enter your Second number. \n"))
print("Enter your choice. \n")
c = input("+ for Addition, - for Substraction, * for Multiplication, / for Division \n")

if c == "+":
    print("Your output is ",a+b)
elif c == "-":
    print("Your output is ",a-b)
elif c == "*":
    print("Your output is ",a*b)
elif c == "/":
    print("Your output is ",a/b)
else:
    print("Wrong input please try again.")