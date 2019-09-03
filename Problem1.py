answer = 0
for index in range(1000):
    if index % 3 == 0 or index % 5 == 0:
        answer += index
print(answer)
