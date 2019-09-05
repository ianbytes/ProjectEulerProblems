number_array = []
end_index = 600851475143
loop_control = True
count = 0

while loop_control:
    for index in range(2, end_index + 1):
        count += 1
        if end_index / index == 1:
            number_array.append(index)
            loop_control = False
            break
        if end_index % index == 0:
            number_array.append(index)
            end_index = int(end_index / index)
            break

print(number_array)
print("Answer: " + str(number_array[-1]))
print("Loop count: " + str(count))
