a,b= int(input("First number: ")),int(input("Second number: "))
print("The whole part of the quotient between " + str(a) + " and " + str(b) + " is " + str(a//b))
print("while the decimal part of the quotient is " + str((a/b)-divmod(a,b)[0]))