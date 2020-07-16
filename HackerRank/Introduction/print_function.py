lim = int(input("Select an integer between 0 and 150 and watch: "))
if 150 >= lim > 0:
    for lin in range(1, lim + 1):
        print(str(lin), end="")
else:
    print("Invalid number.")
