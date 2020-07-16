n = int(input("Write a positive integer from 1 to 100: "))
if 1 <= n <= 100:
    if n%2 != 0 or 6 <= n <= 20:
        print("Weird")
    else:
        if 2 <= n <= 5 or n> 20:
            print("Not Weird")
else:
    print("Invalid number")