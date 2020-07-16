print("Numbers must be between 1 and 10^10.")
a,b= int(input("First number: ")),int(input("Second number: "))
if 1 <= (a or b) <= 10**10:
    print("The sum of both numbers is " + str(a+b))
    print("The difference of the first and the second number is " + str(a-b))
    print("The product of both numbers is " + str(a*b))
else:
    print("Invalid number(s)")