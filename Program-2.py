a = int(input("Enter an integer: "))

odd = [2*i - 1 for i in range(1, a+1)]

print("Series:", ", ".join(map(str, odd)))
