fib_numbers = [1, 2]
even_sum = 2
next_fib_number = 3
while next_fib_number < 4e6:
    if next_fib_number % 2 == 0:
        even_sum += next_fib_number
    fib_numbers.append(next_fib_number)
    next_fib_number = fib_numbers[-2] + fib_numbers[-1]

print(even_sum)

