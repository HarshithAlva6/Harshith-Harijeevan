def multiples(numbers):
    numbers = {i: 0 for i in range(1, 10)}
    
    for val in values:
        for n in numbers:
            if val % n == 0:
                numbers[n] += 1
        
    return numbers

values = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output = multiples(values)
print(output)  
