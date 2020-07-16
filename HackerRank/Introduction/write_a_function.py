year = int(input("Type the year of your preference between 1900 \nand 10^5 to check if it's a leap year or not: "))
if 10**5 > year > 1900:
    if year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            print(str(year) + " is a leap year.")
        else:
            print(str(year) + " isn't a leap year.")
    else:
        if year%4 == 0:
            print(str(year) + " is a leap year.")
        else:
            print(str(year) + " isn't a leap year.")
else:
    print("Year range is invalid.")