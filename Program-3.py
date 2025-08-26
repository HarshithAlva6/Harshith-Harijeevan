a = int(input("Enter an integer: "))

first = a if a % 2 == 1 else a - 1

odd = [i for i in range(1, first + 1, 2)]

print("Series:", ", ".join(map(str, odd)))
