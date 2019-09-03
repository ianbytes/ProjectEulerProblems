indexPrev = 0
index = 1
indexNew = 0
answer = 0
while index < 4000000:
    print(index)
    if index % 2 == 0:
        answer += index
    indexNew = index + indexPrev
    indexPrev = index
    index = indexNew
print(answer)