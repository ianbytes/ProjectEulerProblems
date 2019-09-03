##This is inefficent way of completing, try to complete when index goes to 1,000,000,000
##Need to review Calculus series to get more efficent way of completing
answer = 0
for index in range(1000):
    if index % 3 == 0 or index % 5 == 0:
        answer += index
print(answer)





