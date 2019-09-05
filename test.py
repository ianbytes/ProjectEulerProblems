number = 36
divisor = 2
count = 0
while number >= divisor:
    if number % divisor == 0:
        number /= divisor
    else:
        divisor += 1
    count += 1
print(divisor)
print(count)