def greatest_divisor(m, n):
    r = m % n

    if r == 0:
        return n
    
    return greatest_divisor(n, r)


num_1 = int(input('Type the first value: '))
num_2 = int(input('Type the second value: '))
result = greatest_divisor(num_1, num_2)

print(f"The greatest divisor for {num_1} and {num_2} is: {result}")
