n = int(input("Choose a positive integer higher than 0: "))
if n > 0:
    for lst in range(0, n, 1):
        print(lst ** 2)
else:
    print("The number must be higher than 0.")